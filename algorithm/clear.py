import os
import sys


def clear(is_ft_printable=True):

    if sys.platform.startswith("linux") or sys.platform == "darwin":
        os.system("clear") #linux or mac
    elif sys.platform in ("win32", "cygwin"):
        os.system("cls")  # windows

    if not is_ft_printable:
        print("The 42 pattern cannot be generated due to the coordinates passed, try different ones larger then (6, 8).")
