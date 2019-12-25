from glob import glob

import aiofiles
import frontmatter
import mistune
import pytz
import sass
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse, StreamingResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')
site = {
    "title": "Friendly Bit - Web development blog",
    "description": "Friendly Bit is a blog by Emil Stenström, a Swedish web developer that occasionally gets ideas of how to improve the internet.",  # NOQA
    "url": "https://friendlybit.com",
    "author": "Emil Stenström",
    "timezone": "Europe/Stockholm",
}

async def homepage(request, format_="html"):
    posts = []
    category = request.path_params.get("category", None)

    for file in sorted(glob("posts/*.md"), reverse=True):
        async with aiofiles.open(file, "r") as f:
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
            post.content = mistune.html(post.content)

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
        scss_files = [
            "styles/normalize.scss",
            "styles/base.scss",
            "styles/highlight.scss",
            "styles/layout.scss",
        ]
        for file in scss_files:
            async with aiofiles.open(file, "r") as f:
                yield sass.compile(string=await f.read())

    return StreamingResponse(generate_css(), media_type="text/css")

async def post(request):
    post_slug = request.path_params['slug']
    potential_files = glob(f"posts/*{post_slug}*.md")
    post_found = False
    for file in potential_files:
        async with aiofiles.open(file, "r") as f:
            post = frontmatter.loads(await f.read())
            post.content = mistune.html(post.content)
            post_url = post.metadata["permalink"]
            if not post_url.endswith(f"/{post_slug}/"):
                continue

            if post_url != request.url.path:
                return RedirectResponse(post.metadata["permalink"], status_code=301)

            post_found = True
            break

    if not post_found:
        raise HTTPException(status_code=404)

    return templates.TemplateResponse('post.html', {
        'post': post,
        'site': site,
        'request': request,
    })

async def feed(request):
    return await homepage(request, format_="atom")

async def contact(request):
    async with aiofiles.open("pages/contact.md", "r") as f:
        post = frontmatter.loads(await f.read())

    post.content = mistune.html(post.content)

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
    Mount("/files", app=StaticFiles(directory='files'), name="static"),
    Route("/{category}/{slug}/", endpoint=post),
]

app = Starlette(debug=True, routes=routes)
