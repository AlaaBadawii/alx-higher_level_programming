#!/usr/bin/python3
"""print_sorted module"""


class MyList(list):
    """class that execute list base class"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
