#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return ('\n'.join(map(lambda x: ''.join(list(
            map(lambda y: '#', range(self.__width)))), range(self.__height))))

    def __repr__(self):
        return ("Rectangle({0}, {1})".format(self.__width, self.__height))
