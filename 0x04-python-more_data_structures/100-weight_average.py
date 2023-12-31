#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0 or not isinstance(my_list, list):
        return (0)

    avg = 0
    size = 0
    for tuple in my_list:
        avg += (tuple[0] * tuple[1])
        size += tuple[1]
    return (avg / size)
