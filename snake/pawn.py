#-------------------------------------------------------------------------------
# Name:        pawn
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------


class Pawn:
    def __init__(self, position, length, direction_vector):
        cells_list = []
        for i in range(0, length):
            current_cell = position + (direction_vector * (-i))
            cells_list.append(current_cell)
        self.cells = cells_list
        self.current_direction = direction_vector

    def head(self):
        return self.cells[0]

    def advance(self, next_head, increase_size=False):
        self.cells.insert(0, next_head)
        if not increase_size:
            self.cells.pop()
