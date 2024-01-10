#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attribute and method names.
    """
    return dir(obj)
