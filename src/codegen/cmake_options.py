from pathlib import Path
from typing import Dict, List, Final

__all__ = ["auto_cmake_options"]

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "1-Options.cmake"
_SEPARATOR: Final[str] = "#" * 39

_LANGUAGE_MAP: Final[Dict[str, str]] = {
    "C": "C",
    "C++": "CXX",
    "CPP": "CXX",
    "CXX": "CXX",
}


def _get_user_languages() -> List[str]:
    raw_input = input("Enter programming languages (C, C++, etc.): ").strip()
    langs = [lang.strip().upper() for lang in raw_input.split(",") if lang.strip()]

    try:
        return [_LANGUAGE_MAP[lang] for lang in langs]
    except KeyError as e:
        raise ValueError(f"Unsupported language: {e}")


def _get_user_language_standard() -> int | None:
    raw_input = input(
        "Enter the language standard (e.g., 11 for C++11) or leave blank: "
    ).strip()
    return int(raw_input) if raw_input else None


def _generate_language_block(lang: str, standard: int | None) -> str:
    if standard:
        standard_block = f"""\
set(CMAKE_{lang}_STANDARD {standard})
set(CMAKE_{lang}_STANDARD_REQUIRED ON)
set(CMAKE_{lang}_EXTENSIONS OFF)"""
        status_message = (
            f'message(STATUS "INFO: {lang} standard set to ${{CMAKE_{lang}_STANDARD}}")'
        )
    else:
        standard_block = f"# No standard specified for {lang}"
        status_message = f'message(STATUS "INFO: No {lang} standard specified")'

    return f"""\
{_SEPARATOR}

{standard_block}
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${{CMAKE_SOURCE_DIR}})

{_SEPARATOR}

set(CMAKE_{lang}_FLAGS_RELEASE "${{CMAKE_{lang}_FLAGS_RELEASE}} -O3")

{_SEPARATOR}

set(CMAKE_INTERPROCEDURAL_OPTIMIZATION_RELEASE ON)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

{_SEPARATOR}

{status_message}

{_SEPARATOR}
"""


def auto_cmake_options() -> List[str]:
    project_languages = _get_user_languages()
    project_standard = _get_user_language_standard()

    content = "\n".join(
        _generate_language_block(lang, project_standard) for lang in project_languages
    )

    _CMAKE_DIR.mkdir(exist_ok=True)
    _OUTPUT_FILE.write_text(content)

    return project_languages
