#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(x, y)) for x, y in sorted(a_dictionary.items())]
