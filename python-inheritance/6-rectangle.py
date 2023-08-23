#!/usr/bin/python3
"""Define a class BaseGeometry with a public instance method"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from the base class"""

    def __init__(self, width, height):
        """Initializes new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
