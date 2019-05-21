#!/usr/bin/python3
class Square:
    """ This is the Square class """
    area = 0
    def __init__(self, size=0):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
        self.__size = size


    def area(self):
        """ Example of init method """
        return self.__size * self.__size

    @property
    def size(self):
        """Example of init method"""
        return self.__size
    @size.setter
    def size(self, value):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
        if type(value) is not int :
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
