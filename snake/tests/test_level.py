#-------------------------------------------------------------------------------
# Name:        test_level
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import unittest
import snake.level

class TestLevel(unittest.TestCase):
    def test_empty_level(self):
        level_loader = snake.level.LevelLoader()
        empty_level = level_loader.create_empty_level()
        self.assertEqual(empty_level.width, 64)
        self.assertEqual(empty_level.height, 24)
        cur_table = empty_level.table
        for i in range(2, 63):
            for j in range(2,23):
                self.assertEqual(cur_table[i][j], snake.level.Level.CELL_EMPTY)

if __name__ == '__main__':
    unittest.main()