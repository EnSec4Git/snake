#-------------------------------------------------------------------------------
# Name:        level
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import copy

import snake.geometry as geometry

class LevelLoader:
    def create_empty_level(self, width=64, height=24):
        level = Level()
        table = []
        first_row = [Level.CELL_WALL] * height
        table.append(first_row)
        for i in range(1, width-1):
            current_row = [Level.CELL_WALL]
            current_row.extend([Level.CELL_EMPTY]*(height-2))
            current_row.append(Level.CELL_WALL)
            table.append(current_row)
        last_row = copy.copy(first_row)
        table.append(last_row)
        table[1][1] = Level.CELL_APPLE
        level._set_table(table)
        level.topology = Level.TOPOLOGY_RECTANGLE
        level._starting_positions = [geometry.Point(width//2,1)]
        level._apple_count = 1
        return level

    def create_random_level(self):
        pass

    def load_level_from_file(self, filename):
        pass

class Level:
    CELL_WALL = 1
    CELL_APPLE = 2
    CELL_EMPTY = 3
    CELL_SNAKE = 4

    TOPOLOGY_RECTANGLE = 1
    TOPOLOGY_HORIZONTAL_CYLINDER = 2
    TOPOLOGY_VERTICAL_CYLINDER = 3
    TOPOLOGY_TORUS = 4

    def __init__(self, table=None, starting_positions = []):
        self._table = table
        self._starting_positions = starting_positions
        self._apple_count = 0

    def _cell_for_point(self, point):
        return self.table[point.x][point.y]

    def player_starting_position(self, player_number):
        return self._starting_positions[player_number]

    def remove_apple(self, point):
        self._table[point.x][point.y] = Level.CELL_EMPTY
        self._apple_count -= 1

    def has_apples(self):
        return self._apple_count > 0

    @property
    def table(self):
        return self._table

    def _set_table(self, table):
        self._table = table
        self.width = len(table)
        if(self.width):
            self.height = len(table[0])
        else:
            self.height = 0

    def next_cell(self, point, direction):
        next_point = point + direction
        cell = self._cell_for_point(next_point)
        if cell == Level.CELL_EMPTY or cell == Level.CELL_APPLE:
            return next_point
        elif cell == Level.CELL_SNAKE:
            return None
        if self.topology == Level.TOPOLOGY_RECTANGLE:
            return None
        elif self.topology == Level.TOPOLOGY_HORIZONTAL_CYLINDER:
            if direction.x == 0:
                return Point(next_point.x, next_point.y  % self.height)
            else:
                return None
        elif self.topology == Level.TOPOLOGY_VERTICAL_CYLINDER:
            if direction.y == 0:
                return Point(next_point.x % self.width, next_point.y)
            else:
                return None
        elif self.topology == Level.TOPOLOGY_TORUS:
            return Point(next_point.x % self.width, next_point.y % self.height)
        else:
            raise NotImplementedError("Custom topology not implemented")
