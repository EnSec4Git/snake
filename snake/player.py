#-------------------------------------------------------------------------------
# Name:        player
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

class Player:
    HUMAN_PLAYER = 1

    PLAYER_ACTION_LEFT=1
    PLAYER_ACTION_RIGHT=2
    PLAYER_ACTION_UP=3
    PLAYER_ACTION_DOWN=4

    def get_next_move(self, state):
        raise NotImplementedError("get_next_move called on Abstract Base Class Player")