#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        item = 0
        for item in range(x):
                try:
                        print("{0}".format(my_list[item]), end='')
                except IndexError:
                        print("")
                        return item
        print("")
        return item + 1
