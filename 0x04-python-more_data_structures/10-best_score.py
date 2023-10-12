#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None

    big_key = None
    for key in a_dictionary.keys():
        if big_key is None:
            big_key = key
        elif a_dictionary[key] > a_dictionary[big_key]:
            big_key = key
    return big_key
