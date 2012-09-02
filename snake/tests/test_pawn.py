#-------------------------------------------------------------------------------
# Name:        test_pawn
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import unittest

import snake.pawn
import snake.geometry as geometry


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.__starting_point = geometry.Point(2, 2)
        self.__direction_vector = geometry.FreeVector(1, 0)
        self.__starting_length = 4

    def test_head(self):
        pawn = snake.pawn.Pawn(self.__starting_point, self.__starting_length,\
         self.__direction_vector)
        self.assertEqual(pawn.head(), self.__starting_point)

    def test_length(self):
        pawn = snake.pawn.Pawn(self.__starting_point, self.__starting_length,\
         self.__direction_vector)
        self.assertEqual(len(pawn.cells), self.__starting_length)
        new_head = geometry.Point(3, 2)
        pawn.advance(new_head)
        self.assertEqual(len(pawn.cells), self.__starting_length)
        new_head = geometry.Point(4, 2)
        pawn.advance(new_head, True)
        self.assertEqual(len(pawn.cells), self.__starting_length + 1)

    def test_equality(self):
        pawn = snake.pawn.Pawn(self.__starting_point, self.__starting_length,\
         self.__direction_vector)
        second_pawn = snake.pawn.Pawn(self.__starting_point,\
         self.__starting_length, self.__direction_vector)
        self.assertEqual(pawn, second_pawn)
        third_pawn = snake.pawn.Pawn(self.__starting_point + \
         geometry.FreeVector(1, 0), self.__starting_length,\
         self.__direction_vector)
        self.assertNotEqual(pawn, third_pawn)

if __name__ == '__main__':
    unittest.main()
