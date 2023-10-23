#!/usr/bin/python3

from sys import stderr, exc_info

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return None
