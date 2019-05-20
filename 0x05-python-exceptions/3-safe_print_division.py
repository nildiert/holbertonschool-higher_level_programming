#!/usr/bin/python3
def safe_print_division(a, b):
    division = None
    try:
        division = a / b
        return division
    except ZeroDivisionError:
        return (None)
    finally:
        print('Inside result: {0}'.format(division))
