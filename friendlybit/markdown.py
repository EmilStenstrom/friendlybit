import re
import mistune
import pygments
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from friendlybit.utils import slugify

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
    def link(self, text, url, title=None, **kwargs):
        def is_relative(url):
            return not url.startswith("http") and not url.startswith("//")

        if is_relative(url) and url.startswith("/files/"):
            return f'<a href="{url}" data-no-instant>{text}</a>'

        return super().link(text, url, title)

    def block_code(self, code, info=None):
        lang = info
        match = re.match(r"(.+) \{(.+)\}", lang) if lang else False
        if match:
            lang, class_ = match.groups()

        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = IncludeLangHtmlFormatter(lang=lang)
            html = pygments.highlight(code, lexer, formatter)
        else:
            html = f'<pre>{code}</pre>'

        if match:
            return f'<div class="{class_[1:]}">{html}</div>'
        return html

    def codespan(self, code, **kwargs):
        match = re.match(r"(.+) \{(.+)\}", code)
        if match:
            code, class_ = match.groups()

        html = f'<code>{code}</code>'

        if match:
            return f'<span class="{class_[1:]}">{html}</span>'

        return html

    def heading(self, text, level, **kwargs):
        tag = f'h{level}'
        heading_id = ""
        heading_class = ""

        # Support markdown headings with ids and classes
        match = re.match(r"(.+) \{([^.}]+)(\.[^}]+)?\}", text)
        if match:
            text, heading_id, heading_class = match.groups()
            heading_id = heading_id[1:]  # Remove leading #
            heading_class = heading_class[1:]  # Remove leading .

        if not heading_id:
            heading_id = slugify(text[:50])

        return (
            f'<{tag} id="{heading_id}"'
            + ("" if not heading_class else ' class="' + heading_class + '"')
            + '>'
            + text
            + f'<a href="#{heading_id}">#</a>'
            + f'</{tag}>\n'
        )


markdown = mistune.create_markdown(
    renderer=HighlightRenderer(),
    plugins=['strikethrough', 'table'],
)
