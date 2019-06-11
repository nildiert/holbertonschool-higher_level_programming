#!/usr/bin/python
""" Class Base """
import json


class Base:

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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

#    def save_to_file(cls, list_objs):
#    """ Method to save files  """
#        name = cls + ".json"
#        print(list_objs)
#        with open(name, encoding="utf-8", mode='w') as myFile:
#           myFile.write(cls.to_json_string(list_objs))
