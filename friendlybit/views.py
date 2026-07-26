import re
from datetime import datetime
from glob import glob

import aiofiles
import frontmatter
import pytz
import sass
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse, Response, StreamingResponse
from starlette.templating import Jinja2Templates

from friendlybit.utils import slugify
from friendlybit.markdown import markdown
from friendlybit.settings import scss_files, site

templates = Jinja2Templates(directory='templates')

def alternate_link(url, media_type):
    return f'<{url}>; rel="alternate"; type="{media_type}"'

def accepted_quality(accept, media_type):
    requested_type, requested_subtype = media_type.split("/")
    quality = 0.0

    for item in accept.split(","):
        parts = [part.strip() for part in item.split(";")]
        candidate = parts[0].lower()
        try:
            candidate_type, candidate_subtype = candidate.split("/", 1)
        except ValueError:
            continue

        if candidate_type not in ("*", requested_type):
            continue
        if candidate_subtype not in ("*", requested_subtype):
            continue

        candidate_quality = 1.0
        for parameter in parts[1:]:
            if parameter.lower().startswith("q="):
                try:
                    candidate_quality = float(parameter[2:])
                except ValueError:
                    candidate_quality = 0.0
        quality = max(quality, candidate_quality)

    return quality

def wants_markdown(request):
    accept = request.headers.get("accept", "*/*")
    markdown_quality = accepted_quality(accept, "text/markdown")
    html_quality = accepted_quality(accept, "text/html")
    explicitly_requested = any(
        item.split(";", 1)[0].strip().lower() == "text/markdown"
        for item in accept.split(",")
    )

    if markdown_quality == 0 and html_quality == 0:
        raise HTTPException(status_code=406)

    return (
        explicitly_requested
        and markdown_quality > 0
        and markdown_quality >= html_quality
    )

def markdown_response(content, html_url):
    headers = {
        "Link": alternate_link(html_url, "text/html"),
        "Vary": "Accept",
    }
    return Response(
        content,
        media_type="text/markdown",
        headers=headers,
    )

async def load_post(post_slug):
    for filename in glob(f"posts/*{post_slug}*.md"):
        async with aiofiles.open(filename, "r") as f:
            source = await f.read()
            post = frontmatter.loads(source)
            if post.metadata["permalink"].endswith(f"/{post_slug}/"):
                return post

    raise HTTPException(status_code=404)

def post_as_markdown(post):
    details = [f"# {post.metadata['title']}"]
    if post.metadata.get("date"):
        details.append(f"Published: {post.metadata['date'].strftime('%Y-%m-%d')}")
    if post.metadata.get("author"):
        details.append(f"Author: {post.metadata['author']}")
    return "\n\n".join(details) + "\n\n" + post.content.lstrip()

async def homepage(request, format_="html"):
    post_id = request.query_params.get("p", None)
    if post_id:
        return await redirect_to_slug(request, post_id=post_id)

    posts = []
    category = request.path_params.get("category", None)

    for filename in sorted(glob("posts/*.md"), reverse=True):
        async with aiofiles.open(filename, "r") as f:
            post = frontmatter.loads(await f.read())
            post.metadata["date"] = pytz.timezone(site["timezone"]).localize(post.metadata["date"])

            if category:
                post_categories = [
                    slugify(category)
                    for category in post.metadata["categories"]
                ]
                if category not in post_categories:
                    continue

            posts.append(post)

    if not posts:
        raise HTTPException(status_code=404, detail=f"Posts matching {request.url.path} not found")

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

    raise HTTPException(status_code=415, detail=f"Format {format_} not supported.")

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
    post = await load_post(post_slug)
    post_url = post.metadata["permalink"]
    if post_url != request.url.path:
        return RedirectResponse(post_url, status_code=301)
    if wants_markdown(request):
        return markdown_response(post_as_markdown(post), post_url)
    post.content = markdown(post.content)

    comments = []
    try:
        comment_files = glob(f"comments/*{post_slug}*_comments.md")
        if not comment_files:
            raise FileNotFoundError
        comment_filename = comment_files[0]
        async with aiofiles.open(comment_filename, "r") as f:
            comment_post = frontmatter.loads(await f.read())
            comments = comment_post.metadata.get("comments", [])
            for comment in comments:
                comment["comment_date"] = datetime.strptime(comment["comment_date"], '%Y-%m-%d %H:%M:%S')
    except FileNotFoundError:
        pass

    response = templates.TemplateResponse('post.html', {
        'post': post,
        'comments': comments,
        'site': site,
        'request': request,
    })
    markdown_url = request.url_for(
        "post_markdown",
        category=request.path_params["category"],
        slug=post_slug,
    )
    response.headers["Link"] = alternate_link(markdown_url, "text/markdown")
    response.headers["Vary"] = "Accept"
    return response

async def post_markdown(request):
    post = await load_post(request.path_params["slug"])
    html_url = post.metadata["permalink"]
    expected_markdown_path = html_url.rstrip("/") + ".md"
    if expected_markdown_path != request.url.path:
        return RedirectResponse(expected_markdown_path, status_code=301)
    return markdown_response(post_as_markdown(post), html_url)

async def feed(request):
    return await homepage(request, format_="atom")

async def contact(request):
    async with aiofiles.open("pages/contact.md", "r") as f:
        post = frontmatter.loads(await f.read())

    if wants_markdown(request):
        return markdown_response(post_as_markdown(post), "/contact/")

    post.content = markdown(post.content)
    response = templates.TemplateResponse('page.html', {
        'post': post,
        'site': site,
        'request': request,
    })
    response.headers["Link"] = alternate_link(
        request.url_for("contact_markdown"),
        "text/markdown",
    )
    response.headers["Vary"] = "Accept"
    return response

async def contact_markdown(request):
    async with aiofiles.open("pages/contact.md", "r") as f:
        post = frontmatter.loads(await f.read())
    return markdown_response(post_as_markdown(post), "/contact/")

async def redirect_to_slug(request, post_id):
    for filename in sorted(glob("posts/*.md"), reverse=True):
        print(filename)
        async with aiofiles.open(filename, "r") as f:
            post = frontmatter.loads(await f.read())
            if post.metadata["id"] == int(post_id):
                slug = re.sub(r"/[^/]+/([^/]+)/", r"\1", post.metadata["permalink"])
                category = slugify(post.metadata["categories"][0])
                url = request.url_for("post", category=category, slug=slug)
                return RedirectResponse(url=url)

    return Response(f"Post with {post_id} not found.", status_code=404)
