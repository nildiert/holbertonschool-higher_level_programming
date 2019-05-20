#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        item = 0
        count = 0
        for item in range(x):
                try:
                        print("{0}".format(my_list[item]), end='')
                        count += 1
                except IndexError:
                        print("")
                        return count
        print("")
        return count
