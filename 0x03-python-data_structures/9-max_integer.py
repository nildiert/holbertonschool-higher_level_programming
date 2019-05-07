#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    for it in my_list:
        if it > max:
            max = it
    return max if my_list is not [] else None
