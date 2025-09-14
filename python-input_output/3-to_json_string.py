#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an object."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        A string containing the JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
