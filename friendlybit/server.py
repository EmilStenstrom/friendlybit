from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from friendlybit.views import homepage, favicon, css, feed, contact, post

routes = [
    Route("/", endpoint=homepage, name="homepage"),
    Route("/articles/{category}/", endpoint=homepage, name="category"),
    Route("/favicon.ico", endpoint=favicon, name="favicon"),
    Route("/style.css", endpoint=css, name="css"),
    Route("/feed/", endpoint=feed, name="feed"),
    Route("/feed/{category}/", endpoint=feed, name="feed_category"),
    Route("/contact/", endpoint=contact, name="contact"),
    Mount("/files", app=StaticFiles(directory='files', html=True), name="static"),
    Mount("/images", app=StaticFiles(directory='images', html=True), name="images"),
    Route("/{category}/{slug}/", endpoint=post, name="post"),
]

app = Starlette(debug=True, routes=routes)
