#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    Args:
        obj (object): object
        a_class (class): class
    Returns:
        returns True or false
    """
    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
