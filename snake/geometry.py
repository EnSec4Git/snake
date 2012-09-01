#-------------------------------------------------------------------------------
# Name:        geometry
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GLPv3
#-------------------------------------------------------------------------------

import math

class Point:
    """A class representing a point with integer coordinates.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return Point(x,y)

    def __mod__(self, n):
        x = self.x % n
        y = self.y % n
        return Point(x,y)

    @staticmethod
    def vector_from_points(first_point, second_point):
        dx = second_point.x - first_point.x
        dy = second_point.y - first_point.y
        return FreeVector(dx, dy)

    def __repr__(self):
        return "Point with coordinates: {0}, {1}".format(self.x, self.y)

class FreeVector:
    """A class representing a free vector,
    that is either horizontal or vertical.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, factor):
        x = self.x * factor
        y = self.y * factor
        return FreeVector(x, y)

    def __add__(self, other_vector):
        return FreeVector(self.x + other_vector.x, self.y + other_vector.y)

    def __eq__(self, other_vector):
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        return False

    def length(self):
        assert((self.x == 0) or (self.y == 0))
        return abs(self.x) + abs(self.y)

    def normalize(self):
        length = self.length()
        self.x //= length
        self.y //= length

    def __repr__(self):
        return "FreeVector with coordinates: {0}, {1}".format(self.x, self.y)
