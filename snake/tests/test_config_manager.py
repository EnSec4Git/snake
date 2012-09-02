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
    def test_configuration_manager(self):
        configuration_manager = config_manager.ConfigurationManager()
        self.assertIsInstance(configuration_manager.get_player_count(), int)

if __name__ == '__main__':
    unittest.main()