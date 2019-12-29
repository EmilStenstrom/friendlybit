import os

scss_files = [
    "styles/normalize.scss",
    "styles/base.scss",
    "styles/highlight.scss",
    "styles/layout.scss",
]

site = {
    "title": "Friendly Bit - Web development blog",
    "description": "Friendly Bit is a blog by Emil Stenström, a Swedish web developer that occasionally gets ideas of how to improve the internet.",  # NOQA
    "url": "https://friendlybit.com",
    "author": "Emil Stenström",
    "timezone": "Europe/Stockholm",
    "style_hash": sum([int(os.path.getmtime(filename)) for filename in scss_files]),
    "google_analytics": "UA-67394-2",
}
