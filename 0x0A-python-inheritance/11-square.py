#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """__init__"""
        self.__size = size
        Rectangle.__init__(self, size, size)
        Rectangle.integer_validator(self, "size", size)
        self.__area = self.__size * self.__size

    def area(self):
        """area"""
        return(self.__area)

    def __str__(self):
        """__str__"""
        return"[Square] {:d}/{:d}".format(self.__size, self.__size)
