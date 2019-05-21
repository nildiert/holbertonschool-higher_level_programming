#!/usr/bin/python3
class Square:
    """ This is the Square class """
    def __init__(self, size=0):
        """Example of init method
        Args:
        size (int): Size of the square object
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise
