#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    strlen = len(sys.argv)
    if strlen == 1:
        print("0 arguments.")
    else:
        print("{:d} argument:".format(strlen - 1))
        for i in range(strlen - 1):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
