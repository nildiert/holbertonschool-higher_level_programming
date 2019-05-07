#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    for it in len(my_list):
        if my_list[it] > max:
            max = my_list[it]
    return None if my_list == [] else max
