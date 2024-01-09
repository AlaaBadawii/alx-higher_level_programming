#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string):
    Args:
        my_str (string): string to convert
    Returns:
        returns an object (Python data structure) represented by a JSON string:
    """
    return json.loads(my_str)
