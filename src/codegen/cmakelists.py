from pathlib import Path
from typing import Final

__all__ = ["auto_cmakelists"]

_OUTPUT_FILE: Final[Path] = Path("CMakeLists.txt")


def _generate_content(project_name: str) -> str:
    return f"""\
cmake_minimum_required(VERSION 3.16)
project({project_name})

########################################

list(APPEND CMAKE_MODULE_PATH ${{CMAKE_CURRENT_SOURCE_DIR}}/cmake)

########################################

include(1-Options)
include(2-Optimizations)
include(3-Warnings)
include(4-External)
include(5-Sources)
include(6-Linker)
include(7-Target)

########################################
"""


def auto_cmakelists() -> None:
    project_name = Path.cwd().name
    content = _generate_content(project_name)
    _OUTPUT_FILE.write_text(content)
