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

import snake.level

class State:
    def __init__(self, level, pawns):
        self.level = level
        self.pawns = pawns

    def try_advance(self):
        for (i, pawn) in enumerate(self.pawns):
            if pawn == None:
                print("empty pawn")
                continue
            next_cell = \
                self.level.next_cell(pawn.head(), pawn.current_direction)
            if not next_cell:
                #print("Deleting pawn {0}".format(i))
                self.pawns[i] = None
            else:
                if self.level.table[next_cell.x][next_cell.y] == \
                        snake.level.Level.CELL_APPLE:
                    #print("Apple eaten for pawn {0}".format(i))
                    pawn.advance(next_cell, True)
                    self.level.remove_apple(next_cell)
                else:
                    #print("Standard advance for pawn {0}".format(i))
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