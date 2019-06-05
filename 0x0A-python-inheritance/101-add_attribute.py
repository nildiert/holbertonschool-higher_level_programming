#!/usr/bin/python3
def add_attribute(obj, field, value):
    if (hasattr(obj, '__dict__')):
        setattr(obj, field, value)
    else:
        raise TypeError("can't add new attribute")
