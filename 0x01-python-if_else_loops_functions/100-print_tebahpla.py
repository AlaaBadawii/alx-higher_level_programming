#!/usr/bin/python3
char = 90

for i in range(26):
    if i % 2 == 0:
        char += 32
        
    print("{:c}".format(char), end="")

    if i % 2 == 0:
        char -= 32
    char = char - 1
