from pathlib import Path
from typing import Final

__all__ = ["auto_cmake_linker"]

_CMAKE_DIR: Final[Path] = Path("cmake")
_OUTPUT_FILE: Final[Path] = _CMAKE_DIR / "6-Linker.cmake"

_CONTENT: Final[
    str
] = """\
#######################################

function(apply_linker_optimizations target)
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
        find_program(MOLD_LINKER mold)
        if(MOLD_LINKER)
            get_property(N CACHE PROCESSOR_COUNT PROPERTY VALUE)
            if(NOT N)
                include(ProcessorCount)
                ProcessorCount(N)
            endif()

            if(NOT N EQUAL 0)
                target_link_options(${target} PRIVATE
                    -fuse-ld=mold
                    -Wl,--threads=${N}
                )
                message(STATUS "INFO: using mold linker with ${N} threads for target ${target}")
            endif()
        endif()
    endif()
endfunction()

#######################################
"""


def auto_cmake_linker() -> None:
    _CMAKE_DIR.mkdir(exist_ok=True)
    _OUTPUT_FILE.write_text(_CONTENT)
