#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)

    x = 0
    for i in unique_set:
        x += i

    return x
