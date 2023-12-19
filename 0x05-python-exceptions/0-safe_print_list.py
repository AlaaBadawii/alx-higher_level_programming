#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    real_num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            real_num += 1
        except IndexError:
            print()
            return real_num
    else:
        print()
        return real_num
