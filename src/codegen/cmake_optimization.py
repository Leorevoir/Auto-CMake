from pathlib import Path
from typing import Final

__all__ = ["auto_cmake_optimizations"]

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "2-Optimizations.cmake"

_CONTENT: Final[
    str
] = """\
#######################################

if(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
    find_program(CCACHE_PROGRAM ccache)
    if(CCACHE_PROGRAM)
        set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CCACHE_PROGRAM}")
        set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK "${CCACHE_PROGRAM}")
        message(STATUS "INFO: using ccache: ${CCACHE_PROGRAM}")
    endif()
endif()

#######################################

include(ProcessorCount)
ProcessorCount(N)
if(NOT N EQUAL 0)
    set(CMAKE_BUILD_PARALLEL_LEVEL ${N})
    set(PROCESSOR_COUNT ${N} CACHE INTERNAL "Number of processors")
    message(STATUS "INFO: setting parallel build level to ${N}")
endif()

#######################################
"""


def auto_cmake_optimizations() -> None:
    _CMAKE_DIR.mkdir(exist_ok=True)
    _OUTPUT_FILE.write_text(_CONTENT)
