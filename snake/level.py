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
import ast
import time

import snake.geometry as geometry


class LevelLoader:
    def create_empty_level(self, width=64, height=24):
        level = Level()
        table = []
        first_column = [Level.CELL_WALL] * height
        table.append(first_column)
        for i in range(1, width - 1):
            current_column = [Level.CELL_WALL]
            current_column.extend([Level.CELL_EMPTY] * (height - 2))
            current_column.append(Level.CELL_WALL)
            table.append(current_column)
        last_column = copy.copy(first_column)
        table.append(last_column)
        table[1][1] = Level.CELL_APPLE
        level._set_table(table)
        level.topology = Level.TOPOLOGY_RECTANGLE
        level._starting_positions = [geometry.Point(width // 2, 1)]
        level._apple_count = 1
        return level

    def create_cylinder_level(self, width=64, height=24):
        level = Level()
        table = []
        first_column = [Level.CELL_WALL] * height
        table.append(first_column)
        for i in range(1, width - 1):
            current_column = [Level.CELL_EMPTY] * height
            table.append(current_column)
        last_column = copy.copy(first_column)
        table.append(last_column)
        table[2][2] = Level.CELL_APPLE
        table[62][2] = Level.CELL_APPLE
        level._set_table(table)
        level.topology = Level.TOPOLOGY_VERTICAL_CYLINDER
        level._starting_positions = [geometry.Point(width // 2, 2)]
        level._apple_count = 2
        return level

    def create_random_level(self):
        pass

    def _cell_for_character(self, ch):
        if ch == ' ':
            return Level.CELL_EMPTY
        elif ch == '#':
            return Level.CELL_WALL
        elif ch == 'b':
            return Level.CELL_APPLE

    def load_level_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                line = f.readline()
                opt_dict = ast.literal_eval(line)
                level = Level()
                height = opt_dict['height']
                width = opt_dict['width']
                table_line = [None] * height
                table = [copy.copy(table_line) for i in range(0, width)]
                apple_count = 0
                for (i,line) in enumerate(f):
                    #print(line)
                    for (j,ch) in enumerate(line):
                        if j >= width:
                            break
                        table[j][i] = self._cell_for_character(ch)
                        if table[j][i] == Level.CELL_APPLE:
                            apple_count += 1
                level._apple_count = apple_count
                level._starting_positions = [geometry.Point(width // 2, 2)]
                level._set_table(table)
                level.topology = opt_dict['topology']
                return level
        except IOError:
            return False


class Level:
    CELL_WALL = 1
    CELL_APPLE = 2
    CELL_EMPTY = 3
    CELL_SNAKE = 4

    TOPOLOGY_RECTANGLE = 1
    TOPOLOGY_HORIZONTAL_CYLINDER = 2
    TOPOLOGY_VERTICAL_CYLINDER = 3
    TOPOLOGY_TORUS = 4

    def __init__(self, table=None, starting_positions=[]):
        self._table = table
        self._starting_positions = starting_positions
        self._apple_count = 0

    def _cell_for_point(self, point):
        if (point.x < 0 or point.x >= self.width) or \
            (point.y < 0 or point.y >= self.height):
            return None
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
        elif cell == Level.CELL_SNAKE or cell == Level.CELL_WALL:
            return None
        # By this point, cell should be None and
        # next_point should be outside the box, so we're checking
        # the level topology
        if self.topology == Level.TOPOLOGY_RECTANGLE:
            return None
        elif self.topology == Level.TOPOLOGY_HORIZONTAL_CYLINDER:
            if direction.y == 0:
                #return geometry.Point(next_point.x, (next_point.y + self.height) % self.height)
                return geometry.Point((next_point.x + self.width) % self.width, next_point.y)
            else:
                return None
        elif self.topology == Level.TOPOLOGY_VERTICAL_CYLINDER:
            #print("ASD:", direction, "; ", point, "; ", next_point)
            #time.sleep(1)
            if direction.x == 0:
                #return geometry.Point((next_point.x + self.width) % self.width, next_point.y)
                return geometry.Point(next_point.x, (next_point.y + self.height) % self.height)
            else:
                return None
        elif self.topology == Level.TOPOLOGY_TORUS:
            return geometry.Point((next_point.x + self.width) % self.width, (next_point.y + self.height) % self.height)
        else:
            raise NotImplementedError("Custom topology not implemented")
