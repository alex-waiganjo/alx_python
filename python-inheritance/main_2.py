#!/usr/bin/python3
# Avoid import or from statements inside the comments
BaseGeometry = __import__('3-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))