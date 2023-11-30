#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys

    store_dir = dir(hidden_4)
    for i in store_dir:
        if i[:2] != "__":
            print(i)
