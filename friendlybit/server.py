from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from friendlybit.views import (
    homepage, favicon, css, feed, contact, contact_markdown, post, post_markdown
)

routes = [
    Route("/", endpoint=homepage, name="homepage"),
    Route("/articles/{category}/", endpoint=homepage, name="category"),
    Route("/favicon.ico", endpoint=favicon, name="favicon"),
    Route("/style.css", endpoint=css, name="css"),
    Route("/feed/", endpoint=feed, name="feed"),
    Route("/feed/atom/", endpoint=feed, name="feed"),
    Route("/feed/{category}/", endpoint=feed, name="feed_category"),
    Route("/contact/", endpoint=contact, name="contact"),
    Route("/contact.md", endpoint=contact_markdown, name="contact_markdown"),
    Mount("/script", app=StaticFiles(directory='script', html=True), name="script"),
    Mount("/files", app=StaticFiles(directory='files', html=True), name="static"),
    Mount("/images", app=StaticFiles(directory='images', html=True), name="images"),
    Route("/{category}/{slug}.md", endpoint=post_markdown, name="post_markdown"),
    Route("/{category}/{slug}/", endpoint=post, name="post"),
]

middleware = [
    Middleware(GZipMiddleware, minimum_size=500),
]

app = Starlette(debug=True, routes=routes, middleware=middleware)
