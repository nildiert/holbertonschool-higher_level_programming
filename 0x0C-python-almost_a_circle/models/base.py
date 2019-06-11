#!/usr/bin/python3
""" This is a comment of import """
import json


class Base:
    """ Class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Method to build """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method to convert json to string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
