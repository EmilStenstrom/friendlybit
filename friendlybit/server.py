from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from friendlybit.views import homepage, favicon, css, feed, contact, post

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
