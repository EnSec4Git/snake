#-------------------------------------------------------------------------------
# Name:        pawn
# Purpose:     Provide a game object, controlled by each player
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------


class Pawn:
    """
    A class that contains the physical representation of the snake:
        the cells that it occupies and the direction it is heading.
        This class is pickled as part of the save game process.
    """
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

    def __eq__(self, other_pawn):
        if other_pawn is None:
            return self is None
        if self.cells != other_pawn.cells: return False
        if self.current_direction != other_pawn.current_direction:
            return False
        return True
