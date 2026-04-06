import os
import sys


def clear(is_ft_printable: bool = True) -> None:

    if sys.platform.startswith("linux") or sys.platform == "darwin":
        os.system("clear")
    elif sys.platform in ("win32", "cygwin"):
        os.system("cls")

    if not is_ft_printable:
        print(
            "The 42 pattern cannot be generated due to the coordinates"
            " passed, try different ones larger then (6, 8)."
        )
