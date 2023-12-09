#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        s = k
        y = v * 2
        new_dict[s] = y
    return new_dict
