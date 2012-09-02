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
    ACTION_RESTART = 4
    ACTION_QUIT = 5
    ACTION_NEW_GAME = 6
    ACTION_SAVE = 7
    ACTION_LOAD = 8
    ACTION_OPEN = 9

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
