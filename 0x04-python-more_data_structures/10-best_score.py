#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    biggest = 0
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
            key = k
    return key
