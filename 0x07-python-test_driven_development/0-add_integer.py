#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is not float:
        if type(a) is not int:
            raise TypeError("a must be an integer")
    else:
        int(a)
    if type(b) is not float:
        if type(b) is not int:
            raise TypeError("b must be an integer")
    else:
        int(b)

    return int(a + b)
