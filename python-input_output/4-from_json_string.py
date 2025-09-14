#!/usr/bin/python3
"""Defines a function that returns a Python object from a JSON string."""


def from_json_string(my_str):
    """
    Converts a JSON string into a Python data structure.

    Args:
        my_str: A string containing valid JSON.

    Returns:
        A Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
