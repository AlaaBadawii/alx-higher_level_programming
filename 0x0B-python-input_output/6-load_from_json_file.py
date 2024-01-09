#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    Args:
        filename (file): file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.load(f)
