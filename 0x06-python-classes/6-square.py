#!/usr/bin/python3
""" Square class """


class Square:

    """ This is the Square class """

    def __init__(self, size=0, position=(0, 0)):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
        self.__position = position
        self.__size = size

    def area(self):
        """ Example of init method
        Returns:
            return self.__size * self.__size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Example of init method
        Returns:
            self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Example of init method
        Args:
            size (int): Size of the square object
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(tuple) is not 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                type(value[0]) < 0 or type(value[1]) < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = value

    def my_print(self):
        """Print a square method"""
        if self.__position[1] is not 0:
            print("\n" * self.__position[1], end='')
        for i in range(self.__size):
            print("{}".format(" " * self.__position[0]), end='')
            print("{}".format("#" * self.__size))
