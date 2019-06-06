#!/usr/bin/python3
def class_to_json(obj):
    return dict((obj.__dict__))
