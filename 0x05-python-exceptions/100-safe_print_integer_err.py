#!/usr/bin/python3

from sys import stderr, exc_info

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return False
