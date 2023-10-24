#!/usr/bin/python3
"""SUIIIII"""

class Square:
    """SUIIIII"""
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
        return (self.__size ** 2)

    def __eq__(self, other):
        """SUIIIII"""
        return self.area() == other.area()

    def __ne__(self, other):
        """SUIIIII"""
        return self.area() != other.area()

    def __gt__(self, other):
        """SUIIIII"""
        return self.area() > other.area()

    def __ge__(self, other):
        """SUIIIII"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """SUIIIII"""
        return self.area() < other.area()

    def __le__(self, other):
        """SUIIIII"""
        return self.area() <= other.area()
