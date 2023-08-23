#!/usr/bin/python3
"""Define a class BaseGeometry with a public instance method"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from the base class"""

    def __init__(self, width, height):
        """Initializes new rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints rectangle description [Rectangle] <width>/<height>"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
