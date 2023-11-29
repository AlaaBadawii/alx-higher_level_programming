#!/usr/bin/python3
def islower(c):
    if ord(c) < 91 and ord(c) > 64:
        return False
    elif ord(c) > 96 and ord(c) < 123:
        return True
