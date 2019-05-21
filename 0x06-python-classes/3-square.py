#!/usr/bin/python3
class Square:
    """ This is the Square class """
    def __init__(self, size=0):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
