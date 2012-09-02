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
    def setUp(self):
        self.level_loader = snake.level.LevelLoader()

    def test_empty_level(self):
        empty_level = self.level_loader.create_empty_level()
        self.assertEqual(empty_level.width, 64)
        self.assertEqual(empty_level.height, 24)
        cur_table = empty_level.table
        for i in range(2, 63):
            for j in range(2, 23):
                self.assertEqual(cur_table[i][j], snake.level.Level.CELL_EMPTY)

    def test_create_cylinder_level(self):
        cylinder_level = self.level_loader.create_cylinder_level()
        self.assertEqual(cylinder_level.topology, snake.level.Level.TOPOLOGY_VERTICAL_CYLINDER)

    def test_level_equality(self):
        empty_level_1 = self.level_loader.create_empty_level()
        empty_level_2 = self.level_loader.create_empty_level()
        # Test two copies of same empty level
        self.assertEqual(empty_level_1, empty_level_2)
        # Test identity
        self.assertEqual(empty_level_1, empty_level_1)
        # Test again identity (assert not changed)
        self.assertEqual(empty_level_1, empty_level_1)
        cyl_level_1 = self.level_loader.create_cylinder_level()
        cyl_level_2 = self.level_loader.create_cylinder_level()
        # Test two copies of same cylinder level
        self.assertEqual(cyl_level_1, cyl_level_2)
        # Test identity
        self.assertEqual(cyl_level_1, cyl_level_1)
        # Test again identity (assert not changed)
        self.assertEqual(cyl_level_1, cyl_level_1)

if __name__ == '__main__':
    unittest.main()
