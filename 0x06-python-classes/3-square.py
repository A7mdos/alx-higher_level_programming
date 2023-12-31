#!/usr/bin/python3
"""SUIIIII"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """SUIIIII"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """SUIIIII"""
        return (self.__size * self.__size)
