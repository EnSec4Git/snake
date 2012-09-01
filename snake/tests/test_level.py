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
        self.assertEqual(empty_level.width, 24)
        self.assertEqual(empty_level.height, 64)

if __name__ == '__main__':
    unittest.main()