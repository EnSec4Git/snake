#-------------------------------------------------------------------------------
# Name:        state
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import time

import snake.level


class State:
    """
    This class contains all game-relevant information that is mutated
    during the course of the game: that is the pawns and the level.

    The level is mutated, since apples are removed from it when
    a player eats them.

    The class can be pickled and this is the way Save/Load functionality
    is implemented.
    """
    def __init__(self, level, pawns):
        self.level = level
        self.pawns = pawns

    def try_advance(self):
        for (i, pawn) in enumerate(self.pawns):
            if pawn == None:
                continue
            #print("Head:", pawn.head())
            #time.sleep(0.3)
            next_cell = \
                self.level.next_cell(pawn.head(), pawn.current_direction)
            #print("Next cell:", next_cell)
            #time.sleep(0.3)
            if next_cell == None:
                self.pawns[i] = None
            else:
                if self.level.table[next_cell.x][next_cell.y] == \
                        snake.level.Level.CELL_APPLE:
                    pawn.advance(next_cell, True)
                    self.level.remove_apple(next_cell)
                else:
                    pawn.advance(next_cell)
        if len(self.pawns) > 1 and self._active_count(self.pawns) == 1:
            return self._active_player(self.pawns)
        elif len(self.pawns) == 1:
            if not self.level.has_apples():
                return 0
            elif self._active_count(self.pawns) == 0:
                return -1
        else:
            return True

    def _active_player(self, pawns):
        index = -1
        for (i, pawn) in enumerate(pawns):
            if pawn != None:
                index = i

    def _active_count(self, pawns):
        count = 0
        for pawn in pawns:
            if pawn != None:
                count += 1
        return count
