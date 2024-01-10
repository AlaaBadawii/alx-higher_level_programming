#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified class
    Args:
        obj (object): object
        a_class (class): class
    Returns:
        returns True or false
    """
    return isinstance(obj, a_class) and type(obj) is a_class
