#-------------------------------------------------------------------------------
# Name:        ui
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GLPv3
#-------------------------------------------------------------------------------


class UI:
    """
    This class is an Abstract Base Class (ABC) for the user interface
    of the game. Currently it is inherited only by the ConsoleUI
    class, but any new implementation has to implement only the methods
    put forth in this class.

    An implementation that uses PyQt, for example, or another GUI library
    is feasible.
    """
    ACTION_RESTART = 4
    ACTION_QUIT = 5
    ACTION_NEW_GAME = 6
    ACTION_SAVE = 7
    ACTION_LOAD = 8
    ACTION_OPEN = 9
    ACTION_RANDOM = 10

    def __init__(self, configuration_manager):
        self.configuration_manager = configuration_manager

    def start_listening(self):
        raise NotImplementedError("Called `start_listening` on Abstract Base Class UI instance")

    def stop_listening(self):
        raise NotImplementedError("Called `stop_listening` on Abstract Base Class UI instance")

    def redraw(self, state):
        raise NotImplementedError("Called `redraw` on Abstract Base Class UI instance")

    def get_user_action(self):
        raise NotImplementedError("Called `get_user_action` on Abstract Base Class UI instance")

    def get_player_action(self, i):
        raise NotImplementedError("Called `get_player_action` on Abstract Base Class UI instance")

    def main_menu(self):
        raise NotImplementedError("Called `main_menu` on Abstract Base Class UI instance")

    def display_text(self, text):
        raise NotImplementedError("Called `display_text` on Abstract Base Class UI instance")
