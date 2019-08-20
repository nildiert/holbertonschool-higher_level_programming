#!/usr/bin/python3
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    else:
        max_value = list_of_integers[0]
        for item in list_of_integers:
            if item > max_value:
                max_value = item
        return (max_value)
