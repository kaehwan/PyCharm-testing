import math

def sphere_vol(radius):
    """return the volume of a sphere by providing the radius"""
    return (4/3 * (math.pi)*(radius)**3)

def triangle_area(base, height):
    """return the area of a triangle by providing the base and height"""
    return 0.5*base*height

# 1 inch = 2.54 cm
# 1 foot = 12 inches

def cm(feet=0, inches=0): # two keyword arguments inside this function
    """Converts a length from feet and inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

"""
2 types of arguments when writing a function:
a) keyword argument, which has an equal sign
b) required argument, which doesn't have an equal sign
"""

def plus(x=0, y): # required argument should be put before keyword argument
    return x + y  # else it will generate a SyntaxError