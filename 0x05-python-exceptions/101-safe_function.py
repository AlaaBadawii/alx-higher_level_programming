#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        result = None
    finally:
        return result
