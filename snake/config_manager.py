#-------------------------------------------------------------------------------
# Name:        config_manager
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import snake.player as player
import snake.ui as ui

class ConfigurationManager:
    UI_CONSOLE = 1

    def __init__(self):
        pass

    def get_preferred_UI(self):
        return ConfigurationManager.UI_CONSOLE

    def get_preferred_keys(self):
        return {b'Q':ui.UI.ACTION_QUIT,
                b'R':ui.UI.ACTION_RESTART,
                b'N':ui.UI.ACTION_NEW_GAME}

    def get_preferred_keys_for_player(self, i):
        if i != 0:
            return None
        pl = player.Player
        return {b'A':pl.PLAYER_ACTION_LEFT,
                b'D':pl.PLAYER_ACTION_RIGHT,
                b'W':pl.PLAYER_ACTION_UP,
                b'S':pl.PLAYER_ACTION_DOWN}

    def get_player_count(self):
        return 1

    def get_player_type(self, i):
        return player.Player.HUMAN_PLAYER

    def get_starting_length(self):
        return 4

    def get_iteration_time(self):
        return 0.3