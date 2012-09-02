#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Start the game and run the main menu loop
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
import snake.ui


def main():
    configuration_manager = config_manager.ConfigurationManager()
    if configuration_manager.get_preferred_ui() == config_manager.ConfigurationManager.UI_CONSOLE:
        ui = consoleui.ConsoleUI(configuration_manager)
    while True:
        menu_choice = ui.main_menu()
        if menu_choice == snake.ui.UI.ACTION_NEW_GAME:
            current_game = game.Game(configuration_manager, ui)
            current_game.start_empty_level()
            current_game.loop()
        elif menu_choice == snake.ui.UI.ACTION_QUIT:
            break
        elif menu_choice == snake.ui.UI.ACTION_LOAD:
            current_game = game.Game(configuration_manager, ui)
            savename = ui.get_line("Save name to load: ")
            if current_game.load(savename):
                current_game.loop()
            else:
                ui.display_text("Cannot find saved game")
        elif menu_choice == snake.ui.UI.ACTION_OPEN:
            current_game = game.Game(configuration_manager, ui)
            levelname = ui.get_line("Level name to load: ")
            if current_game.start_loaded_level(levelname):
                current_game.loop()
            else:
                ui.display_text("Level not found")

if __name__ == "__main__":
    main()
