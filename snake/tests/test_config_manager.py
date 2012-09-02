#-------------------------------------------------------------------------------
# Name:        test_config_manager
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
import snake.config_manager as config_manager


class TestConfigurationManager(unittest.TestCase):
    def setUp(self):
        self.__configuration_manager = config_manager.ConfigurationManager()

    def test_player_count(self):
        player_count = self.__configuration_manager.get_player_count()
        self.assertIsInstance(player_count, int)
        self.assertGreaterEqual(player_count, 1)

    def test_iteration_time(self):
        iteration_time = self.__configuration_manager.get_iteration_time()
        self.assertTrue(isinstance(iteration_time, int) or \
         isinstance(iteration_time, float))
        self.assertGreater(iteration_time, 0)

    def test_starting_length(self):
        starting_length = self.__configuration_manager.get_starting_length()
        self.assertIsInstance(starting_length, int)
        self.assertGreaterEqual(starting_length, 1)


if __name__ == '__main__':
    unittest.main()
