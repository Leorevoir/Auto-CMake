from pathlib import Path
from typing import Final

__all__ = ["auto_cmake_target"]

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "7-Target.cmake"
_INCLUDE_DIR_NAME: Final[str] = "include"


def _get_user_target_name(default_name: str) -> str:
    prompt = f"Enter target name (default: {default_name}): "
    return input(prompt).strip() or default_name


def _get_user_target_type() -> str:
    while True:
        prompt = "Is this an EXECUTABLE or a LIBRARY? [EXE/LIB]: "
        raw_type = input(prompt).strip().upper()
        if "EXE".startswith(raw_type):
            return "EXE"
        if "LIB".startswith(raw_type):
            return "LIB"


def _get_user_linked_libs() -> str:
    prompt = "Enter libraries to link (space-separated, e.g., sfml-graphics): "
    return input(prompt).strip()


def _generate_content(
    project_name: str, target_name: str, target_type: str, linked_libs: str
) -> str:
    target_command = "add_executable" if target_type == "EXE" else "add_library"

    if not linked_libs:
        link_block = 'message(STATUS "INFO: No libraries to link.")'
    else:
        link_block = f"""\
target_link_libraries({target_name} PRIVATE {linked_libs})
message(STATUS "INFO: Linking libraries: {linked_libs}")"""

    return f"""\
#######################################

{target_command}({target_name} ${{{project_name}_SOURCES}})
message(STATUS "INFO: Created target '{target_name}' as a {target_type}.")

if(EXISTS "${{CMAKE_CURRENT_SOURCE_DIR}}/{_INCLUDE_DIR_NAME}")
    target_include_directories({target_name} PRIVATE "${{CMAKE_CURRENT_SOURCE_DIR}}/{_INCLUDE_DIR_NAME}")
    message(STATUS "INFO: Added ./{_INCLUDE_DIR_NAME} to the include path for target {target_name}")
endif()

if({project_name}_HEADERS)
    target_sources({target_name} PRIVATE ${{{project_name}_HEADERS}})
endif()

{link_block}

apply_compiler_warnings({target_name})
apply_linker_optimizations({target_name})

#######################################
"""


def auto_cmake_target() -> None:
    project_name = Path.cwd().name
    target_name = _get_user_target_name(project_name)
    target_type = _get_user_target_type()
    linked_libs = _get_user_linked_libs()

    content = _generate_content(project_name, target_name, target_type, linked_libs)

    _CMAKE_DIR.mkdir(exist_ok=True)
    _OUTPUT_FILE.write_text(content)
