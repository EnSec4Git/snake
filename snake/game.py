#-------------------------------------------------------------------------------
# Name:        game
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import time
import pickle

import snake.config_manager
import snake.player
import snake.level as level
import snake.pawn as pawn
import snake.geometry as geometry
import snake.state as state
import snake.human_player as human_player
import snake.ui as ui


class Game:
    """
    This class contains high-level game logic like
    initialization of the level, players, pawns and state.
    """
    LOST_MESSAGE = "You've lost this game."
    WON_MESSAGE = "Player {0} has won."

    def __init__(self, configuration_manager, user_interface):
        self.configuration_manager = configuration_manager
        self.ui = user_interface
        self.player_count = self.configuration_manager.get_player_count()
        self.players = []
        for i in range(0, self.player_count):
            current_player = None
            if configuration_manager.get_player_type(i) == snake.player.Player.HUMAN_PLAYER:
                current_player = human_player.HumanPlayer(self.ui, i)
            self.players.append(current_player)

    def start_empty_level(self):
        level_loader = level.LevelLoader()
        #game_level = level_loader.create_empty_level()
        game_level = level_loader.create_cylinder_level()
        pawns = []
        starting_length = self.configuration_manager.get_starting_length()
        starting_direction = geometry.FreeVector(-1, 0)
        for i in range(0, self.player_count):
            starting_position = game_level.player_starting_position(i)
            game_pawn_i = pawn.Pawn(starting_position, starting_length, starting_direction)
            pawns.append(game_pawn_i)
        self.state = state.State(game_level, pawns)

    def load(self, filename):
        try:
            with open(filename + '.save', 'rb') as f:
                loaded_state = pickle.load(f)
                self.state = loaded_state
                return True
        except IOError:
            return False

    def start_loaded_level(self, filename):
        level_loader = level.LevelLoader()
        game_level = level_loader.load_level_from_file(filename)
        if not game_level:
            return False
        pawns = []
        starting_length = self.configuration_manager.get_starting_length()
        starting_direction = geometry.FreeVector(-1, 0)
        for i in range(0, self.player_count):
            starting_position = game_level.player_starting_position(i)
            game_pawn_i = pawn.Pawn(starting_position, starting_length, starting_direction)
            pawns.append(game_pawn_i)
        self.state = state.State(game_level, pawns)
        return True

    def loop(self):
        time_to_sleep = self.configuration_manager.get_iteration_time()
        pawns = self.state.pawns
        self.ui.start_listening()
        while True:
            user_action = self.ui.get_user_action()
            if user_action == ui.UI.ACTION_QUIT:
                exit(0)
            elif user_action == ui.UI.ACTION_RESTART:
                break
            elif user_action == ui.UI.ACTION_SAVE:
                savename = self.ui.get_line("Name for save: ")
                with open(savename + '.save', 'wb') as f:
                    pickle.dump(self.state, f)
            self.ui.redraw(self.state)
            time.sleep(time_to_sleep)
            for (i, player) in enumerate(self.players):
                player_action = player.get_next_move(self.state)
                if player_action:
                    new_direction = self._direction_for_action(player_action)
                    if not pawns[i].current_direction + new_direction == geometry.FreeVector(0, 0):
                        pawns[i].current_direction = new_direction
            result = self.state.try_advance()
            if result == -1:
                self.ui.display_text(Game.LOST_MESSAGE)
                break
            if isinstance(result, int):
                self.ui.display_text(Game.WON_MESSAGE.format(result))
                break
        self.ui.stop_listening()

    def _direction_for_action(self, action):
        if action == snake.player.Player.PLAYER_ACTION_LEFT:
            return geometry.FreeVector(-1, 0)
        elif action == snake.player.Player.PLAYER_ACTION_DOWN:
            return geometry.FreeVector(0, 1)
        elif action == snake.player.Player.PLAYER_ACTION_UP:
            return geometry.FreeVector(0, -1)
        elif action == snake.player.Player.PLAYER_ACTION_RIGHT:
            return geometry.FreeVector(1, 0)
        else:
            raise AssertionError("Wrong action type")
