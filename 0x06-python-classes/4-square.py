#!/usr/bin/python3
"""SUIIIII"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """SUIIIII"""
        self.size = size

    @property
    def size(self):
        """SUIIIII"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """SUIIIII"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """SUIIIII"""
        return (self.__size * self.__size)
