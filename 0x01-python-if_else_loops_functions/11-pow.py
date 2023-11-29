#!/usr/bin/python3
def pow(a, b):
    result = 1.0
    if b == 0:
        return int(result)
    elif b > 0:
        for i in range(b):
            result *= a
        return int(result)
    else:
        for i in range(-b):
            result /= a
        return result
