#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x, y in dict(a_dictionary).items():
        if value is y:
            del a_dictionary[x]
    return a_dictionary
