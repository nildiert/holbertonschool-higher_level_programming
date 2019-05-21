#!/usr/bin/python3
""" Square class """


class Square:

    """ This is the Square class """

    def __init__(self, size=0, position(0, 0)):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
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

    def my_print(self):
        """Print a square method"""
        if self.__size is not 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
