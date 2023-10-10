#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None or my_list == []:
        return ([])

    is_two_multiple = []
    for num in my_list:
        if num % 2 == 0:
            is_two_multiple.append(True)
        else:
            is_two_multiple.append(False)

    return (is_two_multiple)
