# #!/usr/bin/python3
# """
# Defines a Rectangle subclass Square.
# """
# Rectangle = __import__('9-rectangle').Rectangle


# class Square(Rectangle):
#     """
#     Represent a square.
#     """

#     def __init__(self, size):
#         """
#         Initialize the size of a new square.
#         Args:
#             size (int): private

#         """
#         self.integer_validator("size", size)
#         super().__init__(size, size)
#         self.__size = size

#!/usr/bin/python3
"""
Creates a Square class.
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle (9-rectangle.py).
    Contains a private instance attribute size and a public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square.

        Args:
            size (int): Size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """
        Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2
