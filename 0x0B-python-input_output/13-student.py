#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if attrs is None:
            return dict(self.__dict__)
        else:
            for key in attrs:
                if key in self.__dict__:
                    my_dict.update({key: self.__dict__[key]})

            return my_dict

    def reload_from_json(self, json):
        if json is None:
            return str(self.__dict__)
        else:
            for key, value in json.items():
                self.__dict__.update({key: value})
            print(json)
