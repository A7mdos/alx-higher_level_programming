#!/usr/bin/python3

def no_c(my_string):
    no_c_list = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(no_c_list))
