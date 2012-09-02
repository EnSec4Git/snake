#-------------------------------------------------------------------------------
# Name:        test_state
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import unittest

import os
import pickle

import snake.pawn
import snake.level
import snake.state
import snake.geometry


class TestState(unittest.TestCase):
    def setUp(self):
        self.__starting_point = snake.geometry.Point(2, 2)
        self.__direction_vector = snake.geometry.FreeVector(1, 0)
        self.__starting_length = 4
        self.__pawn = snake.pawn.Pawn(self.__starting_point, self.__starting_length, self.__direction_vector)
        self.__level_loader = snake.level.LevelLoader()
        self.__level = self.__level_loader.create_empty_level()
        self.__temp_filename = "tempfile.pickle"

    def test_pickling(self):
        state = snake.state.State(self.__level, [self.__pawn])
        with open(self.__temp_filename, 'wb') as f:
            pickle.dump(state, f)
        with open(self.__temp_filename, 'rb') as f:
            other_state = pickle.load(f)
        self.assertEqual(state, other_state)

    def tearDown(self):
        os.remove(self.__temp_filename)

if __name__ == '__main__':
    unittest.main()
