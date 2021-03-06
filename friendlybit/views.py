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
