#-------------------------------------------------------------------------------
# Name:        human_player
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import snake.player

class HumanPlayer(snake.player.Player):

    def __init__(self, user_interface, index):
        self.ui = user_interface
        self.index = index

    def get_next_move(self, state):
        #print(self.ui)
        #print(self.index)
        current_action = self.ui.get_player_action(self.index)
        #print(current_action)
        return current_action