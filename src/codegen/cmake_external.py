from pathlib import Path
from typing import Final

__all__ = ["auto_cmake_external"]

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "4-External.cmake"

_CONTENT: Final[
    str
] = """\
#######################################

# TODO: future in a version

#######################################
"""


def auto_cmake_external() -> None:
    _CMAKE_DIR.mkdir(exist_ok=True)
    _OUTPUT_FILE.write_text(_CONTENT)
