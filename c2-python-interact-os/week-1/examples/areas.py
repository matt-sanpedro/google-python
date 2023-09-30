import math

def triangle(base, height):
    """Returns the area of a triangle"""
    return base*height/2

def rectangle(base, height):
    """Returns the area of a rectangle"""
    return base*height

def circle(radius):
    """Returns the area of a circle"""
    return math.pi*(radius**2)

def donut(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)
