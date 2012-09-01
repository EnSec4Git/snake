#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------
import snake.config_manager as config_manager
import snake.game as game
import snake.consoleui as consoleui

def main():
    configuration_manager = config_manager.ConfigurationManager()
    if configuration_manager.get_preferred_UI() == config_manager.ConfigurationManager.UI_CONSOLE:
        ui = consoleui.ConsoleUI(configuration_manager)
    while ui.main_menu():
        current_game = game.Game(configuration_manager, ui)
        current_game.loop()

if __name__ == "__main__":
    main()