from pathlib import Path

import sass

from friendlybit.settings import scss_files


CSS = "".join(
    sass.compile(string=Path(filename).read_text())
    for filename in scss_files
)
