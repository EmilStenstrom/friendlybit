import re
import mistune
import pygments
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

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
    def block_code(self, code, lang=None, **kwargs):
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

    def codespan(self, code, **kwargs):
        match = re.match(r"(.+) \{(.+)\}", code)
        if match:
            code, class_ = match.groups()

        html = f'<code>{mistune.escape(code)}</code>'

        if match:
            return f'<span class="{class_[1:]}">{html}</span>'

        return html

    def heading(self, text, level, **kwargs):
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
