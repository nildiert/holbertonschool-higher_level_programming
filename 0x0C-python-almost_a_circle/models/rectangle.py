#!/usr/bin/python3
""" Class model Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Contructor method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Method to return the with """
        return self.__width

    @width.setter
    def width(self, value):

        """ Method to set the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ Method to return the height """
        return self.__height

    @height.setter
    def height(self, value):

        """ Method to set the  height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """ Method to return the x value  """
        return self.__x

    @x.setter
    def x(self, value):

        """ Method to set the x value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """ Method to return the y value """
        return self.__y

    @y.setter
    def y(self, value):

        """ Method to set the y value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """ Method to calculate the area """
        return self.width * self.height

    def display(self):

        """ Method to print the square """
        print("\n" * self.y, end='')
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):

        """ Method to return the string of the class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):

        """ Method to update the value of the class """
        my_list = ["id", "width", "height", "x", "y"]
        for count, value in enumerate(args):
            setattr(self, my_list[count], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):

        """ Method to convert a object in a dictionary """
        return {"x": self.x, "y": self.y, "height": self.height,
                "width": self.width, "id": self.id}
