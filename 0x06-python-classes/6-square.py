#!/usr/bin/python3
"""SUIIIII"""

class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """SUIIIII"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """SUIIIII"""
        if (not isinstance(value, tuple) or len(value) is not 2 or
            not isinstance(value[0], int) or
                not isinstance(value[1], int) or value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """SUIIIII"""
        return (self.__size ** 2)

    def my_print(self):
        """SUIIIII"""
        if self.__size is not 0:
            for y in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
