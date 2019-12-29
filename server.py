import re
from glob import glob
from datetime import datetime
import os

import aiofiles
import frontmatter
import mistune
import pygments
import pytz
import sass
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse, StreamingResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


class IncludeLangHtmlFormatter(HtmlFormatter):
    def __init__(self, lang=None, **options):
        super().__init__(**options)
        self.lang = lang

    def _wrap_div(self, inner):
        yield 0, (f'<div class="highlight" data-language="{self.lang.upper()}">')
        for tup in inner:
            yield tup
        yield 0, '</div>\n'

class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        match = re.match(r"(.+) \{(.+)\}", lang) if lang else False
        if match:
            lang, class_ = match.groups()

        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = IncludeLangHtmlFormatter(lang=lang)
            html = pygments.highlight(code, lexer, formatter)
        else:
            html = f'<pre>{mistune.escape(code)}</pre>'

        if match:
            return f'<div class="{class_[1:]}">{html}</div>'
        return html

    def codespan(self, code):
        match = re.match(r"(.+) \{(.+)\}", code)
        if match:
            code, class_ = match.groups()

        html = f'<code>{mistune.escape(code)}</code>'

        if match:
            return f'<span class="{class_[1:]}">{html}</span>'

        return html

    def heading(self, text, level):
        tag = f'h{level}'
        match = re.match(r"(.+) \{([^.}]+)(\.[^}]+)?\}", text)
        if match:
            text, id_, class_ = match.groups()
            if class_:
                return f'<{tag} id="{id_[1:]}" class="{class_[1:]}">{text}</{tag}>\n'

            return f'<{tag} id="{id_[1:]}">{text}</{tag}>\n'

        return f'<{tag}>{text}</{tag}>\n'


markdown = mistune.create_markdown(
    renderer=HighlightRenderer(escape=False),
    plugins=['strikethrough', 'table'],
)

scss_files = [
    "styles/normalize.scss",
    "styles/base.scss",
    "styles/highlight.scss",
    "styles/layout.scss",
]

templates = Jinja2Templates(directory='templates')

site = {
    "title": "Friendly Bit - Web development blog",
    "description": "Friendly Bit is a blog by Emil Stenström, a Swedish web developer that occasionally gets ideas of how to improve the internet.",  # NOQA
    "url": "https://friendlybit.com",
    "author": "Emil Stenström",
    "timezone": "Europe/Stockholm",
    "style_hash": sum([int(os.path.getmtime(filename)) for filename in scss_files]),
    "google_analytics": "UA-67394-2",
}

async def homepage(request, format_="html"):
    posts = []
    category = request.path_params.get("category", None)

    for filename in sorted(glob("posts/*.md"), reverse=True):
        async with aiofiles.open(filename, "r") as f:
            post = frontmatter.loads(await f.read())
            post.metadata["date"] = pytz.timezone(site["timezone"]).localize(post.metadata["date"])

            if category:
                post_categories = [
                    category.lower().replace(" ", "-")
                    for category in post.metadata["categories"]
                ]
                if category not in post_categories:
                    continue

            posts.append(post)

    if format_ == "html":
        return templates.TemplateResponse('index.html', {
            'category': category,
            'posts': posts,
            'site': site,
            'request': request,
        })
    elif format_ == "atom":
        for post in posts:
            post.content = markdown(post.content)

        return templates.TemplateResponse('atom.xml', {
            'category': category,
            'posts': posts,
            'site': site,
            'request': request,
        }, media_type="text/xml")

    raise HTTPException(status_code=415, detail=f"Format {format} not supported.")

async def favicon(request):
    return FileResponse('favicon.ico')

async def css(request):
    async def generate_css():
        for filename in scss_files:
            async with aiofiles.open(filename, "r") as f:
                yield sass.compile(string=await f.read())

    return StreamingResponse(generate_css(), media_type="text/css")

async def post(request):
    post_slug = request.path_params['slug']
    potential_files = glob(f"posts/*{post_slug}*.md")
    post_found = False
    for filename in potential_files:
        async with aiofiles.open(filename, "r") as f:
            post = frontmatter.loads(await f.read())
            post.content = markdown(post.content)
            post_url = post.metadata["permalink"]
            if not post_url.endswith(f"/{post_slug}/"):
                continue

            if post_url != request.url.path:
                return RedirectResponse(post.metadata["permalink"], status_code=301)

            post_found = True
            break

    if not post_found:
        raise HTTPException(status_code=404)

    comments = []
    try:
        comment_filename = f"{filename.replace('posts/', 'comments/').rsplit('.', 1)[0]}_comments.md"
        async with aiofiles.open(comment_filename, "r") as f:
            comment_post = frontmatter.loads(await f.read())
            comments = comment_post.metadata.get("comments", [])
            for comment in comments:
                comment["comment_date"] = datetime.strptime(comment["comment_date"], '%Y-%m-%d %H:%M:%S')
    except FileNotFoundError:
        pass

    return templates.TemplateResponse('post.html', {
        'post': post,
        'comments': comments,
        'site': site,
        'request': request,
    })

async def feed(request):
    return await homepage(request, format_="atom")

async def contact(request):
    async with aiofiles.open("pages/contact.md", "r") as f:
        post = frontmatter.loads(await f.read())

    post.content = markdown(post.content)

    return templates.TemplateResponse('page.html', {
        'post': post,
        'site': site,
        'request': request,
    })

routes = [
    Route("/", endpoint=homepage),
    Route("/articles/{category}/", endpoint=homepage),
    Route("/favicon.ico", endpoint=favicon),
    Route("/style.css", endpoint=css),
    Route("/feed/", endpoint=feed),
    Route("/feed/{category}/", endpoint=feed),
    Route("/contact/", endpoint=contact),
    Mount("/files", app=StaticFiles(directory='files', html=True), name="static"),
    Route("/{category}/{slug}/", endpoint=post),
]

app = Starlette(debug=True, routes=routes)
