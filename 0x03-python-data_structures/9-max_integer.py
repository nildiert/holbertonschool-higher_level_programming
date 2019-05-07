#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list is not []:
        my_list.sort(reverse=True)
        max = my_list[0]
        return (max)
    return None
