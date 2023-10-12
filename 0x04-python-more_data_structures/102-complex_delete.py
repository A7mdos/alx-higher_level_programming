#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None

    deleeete = [key for key, val in a_dictionary.items() if val == value]
    for key in deleeete:
        del a_dictionary[key]

    return a_dictionary
