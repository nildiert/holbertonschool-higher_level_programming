#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None and len(my_list) is not 0:
        divided, sumatory = 0, 0
        for tups in my_list:
            sumatory += tups[0] * tups[1]
            divided += tups[1]
        return sumatory / divided
    else:
        return 0
