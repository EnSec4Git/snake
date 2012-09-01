#-------------------------------------------------------------------------------
# Name:        test_geometry
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import unittest
import snake.geometry
import copy

class TestPoint(unittest.TestCase):
    def test_zero_point(self):
        point = snake.geometry.Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_vector_point(self):
        first_point = snake.geometry.Point(2, 3)
        second_point = snake.geometry.Point (4, 3)
        vector = snake.geometry.Point.vector_from_points(first_point, second_point)
        third_point = first_point + vector
        self.assertEqual(vector.x, 2)
        self.assertEqual(vector.y, 0)
        self.assertEqual(second_point.x, third_point.x)
        self.assertEqual(second_point.y, third_point.y)

class TestFreeVector(unittest.TestCase):
    def test_zero_vector(self):
        vector = snake.geometry.FreeVector()
        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 0)
        self.assertEqual(vector.length(), 0)

    def test_normalize_vector(self):
        vector = snake.geometry.FreeVector(6,0)
        self.assertEqual(vector.length(), 6)
        vector.normalize()
        self.assertEqual(vector.length(), 1)

    def test_horizontal_vector(self):
        vector = snake.geometry.FreeVector(-3,0)
        self.assertEqual(vector.x, -3)
        self.assertEqual(vector.y, 0)
        self.assertEqual(vector.length(), 3)
        vector.normalize()
        self.assertEqual(vector.x, -1)
        self.assertEqual(vector.y, 0)

    def test_vertical_vector(self):
        vector = snake.geometry.FreeVector(0,2)
        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 2)
        self.assertEqual(vector.length(), 2)
        vector.normalize()
        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 1)

    def test_irregular_vector(self):
        vector = snake.geometry.FreeVector(2, -3)
        self.assertRaises(AssertionError, vector.length)

    def test_multiply_vector(self):
        vector = snake.geometry.FreeVector(3,0)
        vector.normalize()
        multiplied_vector = vector * 3
        self.assertEqual(vector.length(), 1)
        self.assertEqual(multiplied_vector.length(), 3)
        self.assertEqual(multiplied_vector.x, 3)

if __name__ == '__main__':
    unittest.main()