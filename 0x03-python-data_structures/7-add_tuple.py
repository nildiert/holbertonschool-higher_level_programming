#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

        new_tuple = (0, 0)
        if (tuple_a == 1 and tuple_b):
                return (tuple_a, tuple_b)
        if (tuple_a == ()):
                tuple_a = new_tuple
        if (tuple_b == ()):
                tuple_b = new_tuple
        if len(tuple_a) is 1:
                return (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        if len(tuple_b) is 1:
                return (tuple_a[0] + tuple_b[0], tuple_b[0] + 0)
        if len(tuple_a) >= 2 and len(tuple_b) >= 2:
                return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
