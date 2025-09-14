#!/usr/bin/python3
"""Defines a function that appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
