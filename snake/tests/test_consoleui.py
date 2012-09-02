#-------------------------------------------------------------------------------
# Name:        test_consoleui
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
import snake.consoleui as consoleui

class TestConsoleUI(unittest.TestCase):
    def test_consoleui(self):
        configuration_manager = config_manager.ConfigurationManager()
        console_user_interface = consoleui.ConsoleUI(configuration_manager)
        console_user_interface.start_listening()
        console_user_interface.stop_listening()

if __name__ == '__main__':
    unittest.main()