#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    divisions = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            res = 0
            print("out of range")
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        finally:
            divisions.append(res)

    return divisions
