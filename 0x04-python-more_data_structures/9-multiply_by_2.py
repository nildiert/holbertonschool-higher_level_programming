#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys, values = list(a_dictionary.keys()), list(a_dictionary.values())
    return dict(zip(keys, map(lambda x: x * 2, values)))
