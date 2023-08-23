#!/usr/bin/python3
"""
class Rectangle
"""
from .base import Base


class Rectangle(Base):
    """class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        try:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        except:
            raise

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        try:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        except:
            raise

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        try:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        except:
            raise

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        try:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        except:
            raise

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the character #"""
        for row in range(self.y):
            print()
        for lines in range(self.height):
            print("{}".format(" " * self.x), end="")
            print("{}".format("#" * self.width))

    def __str__(self):
        """method so that it returns """
        new_str = "[Rectangle] ({}) {}/{} - {}/{}"
        return new_str.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update the class and assigns an argument to each attribute:"""
        count = 0
        keys_of_attributes = ["id", "width", "height", "x", "y"]

        for value in args:
            if not count:
                super().__init__(value)
            if count < 5:
                setattr(self, keys_of_attributes[count], value)
            count += 1

        if not args or not len(args):
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(kwargs[key])
                else:
                    setattr(self, key, value)

    def update(self, *args, **kwargs):
        """ Update rectangle class """
        if len(args):
            i = 0
            key = ['id', 'width', 'height', 'x', 'y']
            for value in args:
                if i < 5:
                    setattr(self, key[i], value)
                    i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a rectangle dictionary """
        dic = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dic