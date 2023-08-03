#!/usr/bin/python3
"""
Getting the class instance and should be an integer
"""
class Square:
    """
Getting the class instance
"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2