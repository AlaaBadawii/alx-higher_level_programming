#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as s:
        print("Exception: {}".format(s), file=sys.stderr)
        return False
    except TypeError as b:
        sys.stderr.write(b)
        return False
    else:
        return True
