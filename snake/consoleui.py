#-------------------------------------------------------------------------------
# Name:        consoleui
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GLPv3
#-------------------------------------------------------------------------------

import threading
import os
import copy
import time
import snake.level as level
import snake.ui as ui
import snake.config_manager
import snake.player as player

if os.name in ("nt", "dos", "ce"):
    import msvcrt
elif os.name == "posix":
    pass

class ConsoleUI(ui.UI):
    def __init__(self, configuration_manager):
        super().__init__(configuration_manager)

    def _clear_screen(self, numlines=100):
        """Clears the console screen.
        This code is supposed to work for Unix, Windows and has a fallback for
        other OSes.
        """
        #return
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')
        else:
            # Fallback for other operating systems.
            print('\n' * numlines)

    def start_listening(self):
        self.background_thread = threading.Thread(target=self._background_action, args=())
        self._current_action = None
        self._should_stop = False
        self._current_player_count = \
            self.configuration_manager.get_player_count()
        self._current_player_actions = [None] * self._current_player_count
        self._key_bindings = self.configuration_manager.get_preferred_keys()
        self._player_key_bindings = []
        for i in range(0, self._current_player_count):
            player_i_keys = \
                self.configuration_manager.get_preferred_keys_for_player(i)
            self._player_key_bindings.append(player_i_keys)
        self.background_thread.start()

    def stop_listening(self):
        self._should_stop = True

    def redraw(self, state):
        current_level = state.level
        table = current_level.table
        pawns = state.pawns
        table_to_draw = copy.deepcopy(table)
        for pawn in pawns:
            for cell in pawn.cells:
                table_to_draw[cell.x][cell.y] = level.Level.CELL_SNAKE
        string_to_print = self.__string_for_table(current_level, table_to_draw)
        self._clear_screen()
        print(string_to_print)


    def get_user_action(self):
        cur_action_copy = copy.copy(self._current_action)
        if cur_action_copy == ui.UI.ACTION_QUIT:
            return cur_action_copy
        elif cur_action_copy == ui.UI.ACTION_RESTART:
            return cur_action_copy
        else:
            return None

    def get_player_action(self, i):
        player_action_copy = copy.copy(self._current_player_actions[i])
        return player_action_copy

    def display_text(self, text):
        print(text)

    def main_menu(self):
        pref_keys = self.configuration_manager.get_preferred_keys()
        pref_keys_rev = dict((v,k) for k, v in pref_keys.items())
        print("Press {0} to start, {1} to quit".format(chr(ord(pref_keys_rev[ui.UI.ACTION_NEW_GAME])), chr(ord(pref_keys_rev[ui.UI.ACTION_QUIT]))))
        while True:
            character = self._cp_get_char()
            if character == pref_keys_rev[ui.UI.ACTION_NEW_GAME]:
                return True
            elif character == pref_keys_rev[ui.UI.ACTION_QUIT]:
                return False
            else:
                pass

    def _cp_kbhit(self):
        if os.name == "posix":
            raise NotImplementedError("kbhit not implemented on POSIX yet")
        elif os.name in ("nt", "dos", "ce"):
            return msvcrt.kbhit()
        else:
            raise NotImplementedError("kbhit not implemented")

    def _cp_get_char(self):
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            raise NotImplementedError("get_char not implemented on POSIX yet")
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            return msvcrt.getch()
        else:
            # Fallback for other operating systems.
            raise NotImplementedError("get_char not implemented")

    def _background_action(self):
        while True:
            if self._should_stop:
                return
            time.sleep(0.1)
            if self._cp_kbhit():
                ch = self._cp_get_char()
                #print("New character press:", ch)
                for i in range(0, self._current_player_count):
                    if ch in self._player_key_bindings[i]:
                        current_keys = self._player_key_bindings[i]
                        self._current_player_actions[i] = current_keys[ch]
                if ch in self._key_bindings:
                    self._current_action = self._key_bindings[ch]
                    if self._current_action == ui.UI.ACTION_QUIT:
                        self._should_stop = True
                    elif self._current_action == ui.UI.ACTION_RESTART:
                        self._should_stop = True

    def __string_for_table(self, current_level, table):
        string = ""
        for i in range(current_level.height):
            line = ""
            for j in range(current_level.width):
                cell_char = ''
                cell = table[j][i]
                if cell == level.Level.CELL_EMPTY:
                    cell_char = ' '
                elif cell == level.Level.CELL_WALL:
                    cell_char = '#'
                elif cell == level.Level.CELL_APPLE:
                    cell_char = 'b'
                elif cell == level.Level.CELL_SNAKE:
                    cell_char = 'o'
                line = line + cell_char
            string = string + line + '\n'
        return string