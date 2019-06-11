#!/usr/bin/python3
""" Class Square inherits to Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Contructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Method to return the size value"""
        return super().width

    @size.setter
    def size(self, value):
        """ Method setter for size"""
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def __str__(self):
        """ Method that returns a string of class """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Method to update the values """
        my_list = ["id", "size", "x", "y"]
        for count, value in enumerate(args):
            setattr(self, my_list[count], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Method to convert to dictionary """
        return {"x": self.x, "y": self.y, "size": self.size, "id": self.id}
