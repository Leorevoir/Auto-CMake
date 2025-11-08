from pathlib import Path
from typing import Dict, List, Final

__all__ = ["auto_cmake_sources"]

_SRC_DIR_NAME: Final[str] = "src"
_INCLUDE_DIR_NAME: Final[str] = "include"

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "5-Sources.cmake"

_LANGUAGE_PATTERNS: Final[Dict[str, List[str]]] = {
    "C": ['"${SOURCE_DIR}/*.c"'],
    "CXX": [
        '"${SOURCE_DIR}/*.cpp"',
        '"${SOURCE_DIR}/*.cxx"',
        '"${SOURCE_DIR}/*.cc"',
    ],
}


def _get_source_glob_patterns(languages: List[str]) -> str:
    patterns = [
        pattern for lang in languages for pattern in _LANGUAGE_PATTERNS.get(lang, [])
    ]
    return "\n".join(f"    {p}" for p in patterns)


def _generate_cmake_content(project_name: str, languages: List[str]) -> str:
    source_glob_patterns = _get_source_glob_patterns(languages)

    return f"""\
#######################################

set(SOURCE_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/{_SRC_DIR_NAME}")
set(INCLUDE_DIR "${{CMAKE_CURRENT_SOURCE_DIR}}/{_INCLUDE_DIR_NAME}")

message(STATUS "INFO: Source directory set to ${{SOURCE_DIR}}")
message(STATUS "INFO: Include directory set to ${{INCLUDE_DIR}}")

file(GLOB_RECURSE {project_name}_SOURCES
{source_glob_patterns}
)

if(EXISTS ${{INCLUDE_DIR}})
    file(GLOB_RECURSE {project_name}_HEADERS
        "${{INCLUDE_DIR}}/*.h"
        "${{INCLUDE_DIR}}/*.hpp"
    )
endif()

message(STATUS "INFO: Found sources for compilation: ${{{project_name}_SOURCES}}")
if({project_name}_HEADERS)
    message(STATUS "INFO: Found headers for IDE: ${{{project_name}_HEADERS}}")
endif()

#######################################
"""


def auto_cmake_sources(languages: List[str]) -> None:
    project_name = Path.cwd().name
    content = _generate_cmake_content(project_name, languages)

    Path(_SRC_DIR_NAME).mkdir(exist_ok=True)
    Path(_INCLUDE_DIR_NAME).mkdir(exist_ok=True)

    _OUTPUT_FILE.write_text(content)
