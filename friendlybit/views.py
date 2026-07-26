from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse, Response
from starlette.templating import Jinja2Templates

from friendlybit.content import (
    all_posts,
    category_posts,
    comments_for_slug,
    contact_page,
    post_by_id,
    post_by_slug,
)
from friendlybit.markdown import markdown
from friendlybit.settings import site
from friendlybit.styles import CSS

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
    post = post_by_slug(post_slug)
    if not post:
        raise HTTPException(status_code=404)
    return post

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

    category = request.path_params.get("category", None)
    posts = category_posts(category) if category else all_posts()

    if not posts:
        raise HTTPException(status_code=404, detail=f"Posts matching {request.url.path} not found")

    if format_ == "html":
        return templates.TemplateResponse(request=request, name='index.html', context={
            'category': category,
            'posts': posts,
            'site': site,
            'request': request,
        })
    elif format_ == "atom":
        posts = posts[:site["feed_posts"]]
        for post in posts:
            post.content = markdown(post.content)

        return templates.TemplateResponse(request=request, name='atom.xml', context={
            'category': category,
            'posts': posts,
            'site': site,
            'request': request,
        }, media_type="text/xml")

    raise HTTPException(status_code=415, detail=f"Format {format_} not supported.")

async def favicon(request):
    return FileResponse('favicon.ico')

async def css(request):
    return Response(CSS, media_type="text/css")

async def post(request):
    post_slug = request.path_params['slug']
    post = await load_post(post_slug)
    post_url = post.metadata["permalink"]
    if post_url != request.url.path:
        return RedirectResponse(post_url, status_code=301)
    if wants_markdown(request):
        return markdown_response(post_as_markdown(post), post_url)
    post.content = markdown(post.content)

    comments = comments_for_slug(post_slug)

    response = templates.TemplateResponse(request=request, name='post.html', context={
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
    post = contact_page()

    if wants_markdown(request):
        return markdown_response(post_as_markdown(post), "/contact/")

    post.content = markdown(post.content)
    response = templates.TemplateResponse(request=request, name='page.html', context={
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
    post = contact_page()
    return markdown_response(post_as_markdown(post), "/contact/")

async def redirect_to_slug(request, post_id):
    post = post_by_id(int(post_id))
    if post:
        return RedirectResponse(url=post.metadata["permalink"])

    return Response(f"Post with {post_id} not found.", status_code=404)
