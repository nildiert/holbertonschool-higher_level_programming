#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list == []:
        return None
    else:
        for item in my_list:
            new_list.append(item % 2 == 0)
    return (new_list)
