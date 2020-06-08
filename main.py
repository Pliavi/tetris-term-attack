import random
import time
import readchar
from resources import *
from helpers import *
from typing import List
from enum import IntEnum
from itertools import chain


class Axis(IntEnum):
    COL = 1
    ROW = 0


class Game(object):
    """
        action_queue: is the diff queue in the board that
                     is dispatched each "frame"
    """
    board: List[List[int]] = []
    board_size: List[int] = [0, 0]
    cursor_pos: List[int] = [0, 0]
    ticks: int = 0
    game_finished: bool = False
    action_queue: List[List[int]] = []
    controller_keys = {
        "move": [
            readchar.key.UP,
            readchar.key.RIGHT,
            readchar.key.DOWN,
            readchar.key.LEFT,
        ]
    }

    def __init__(self, board_size=[15, 6]):
        self.board_size = board_size
        self.setup()

    def setup(self):
        for y in range(self.board_size[Axis.ROW]):
            self.board.append([])
            for x in range(self.board_size[Axis.COL]):
                self.board[y].append(0)

    def update_screen(self,):
        pass

    def print_screen(self):
        for index, line in enumerate(self.board):
            print(f"{index:2}|", *line)

    def update_board(self,):
        pass

    def dispatch_actions(self):
        print(self.action_queue)
        for action in self.action_queue:
            action_name = action["action"]
            if action_name == "piece_drop":
                pass
            if action_name == "piece_swap":
                for diff in action["diffs"]:
                    self.board[diff[0]][diff[1]] = diff[2]
                # TODO: Check about "del self.action_queue[-1]"
                self.action_queue.pop()
                self.print_screen()
            if action_name == "cursor_updated":
                pass

    def add_line_below(self,):
        line = []
        for _ in range(self.board_size[Axis.COL]):
            random_piece_index = random.randint(1, 5)
            line.append(random_piece_index)

        self.board.insert(0, line)

    def remove_line_above(self,):
        del self.board[-1]

    def check_matches(self):
        pass

    def run_in_board(self, callback_to_cells=None, callback_to_rows=None):
        diffs = []
        for row_index, row in enumerate(self.board):
            if callback_to_rows:
                callback_to_rows(row_index, row)
            for cell_index, cell in enumerate(self.board[row_index]):
                if callback_to_cells:
                    diffs.append(callback_to_cells(
                        cell_index, cell, row_index, row))
        return chain.from_iterable(diffs)

    def queue_drops(self):
        def do_drops(cell_index, cell, row_index, line):
            is_first_row = row_index == 0
            if not(is_first_row) and board[row_index][cell_index] != BlockIndex.EMPTY:
                next_possibly_empty_row = row_index
                while True:  # NÃO EXISTE DO..WHILE EM PYTHON!!
                    next_possibly_empty_row -= 1
                    if self.board[next_possibly_empty_row][cell_index] != BlockIndex.EMPTY:
                        return [[row_index, cell_index, BlockIndex.EMPTY],
                                [next_possibly_empty_row, cell_index, cell]]

        diffs = self.run_in_board(do_drops)
        self.action_queue.append({
            "action": "piece_drop",
            "diffs": diffs
        })

    def swap_piece(self):
        piece_position = self.cursor_pos

        current_piece_row = piece_position[Axis.ROW]
        current_piece_col = piece_position[Axis.COL]

        current_piece = self.board[current_piece_row][current_piece_col]
        swap_piece = self.board[current_piece_row][current_piece_col + 1]

        self.action_queue.append({
            "action": "piece_swap",
            "diffs": [
                [current_piece_row, current_piece_col + 1, current_piece],
                [current_piece_row, current_piece_col, swap_piece]
            ]
        })

    def move_cursor(self, pressed_key):
        if pressed_key == readchar.key.UP:
            self.cursor_pos[Axis.COL] += 1
        if pressed_key == readchar.key.DOWN:
            self.cursor_pos[Axis.COL] -= 1
        if pressed_key == readchar.key.LEFT:
            self.cursor_pos[Axis.ROW] -= 1
        if pressed_key == readchar.key.RIGHT:
            self.cursor_pos[Axis.ROW] += 1

        self.action_queue.append({"action": "cursor_updated"})

    def play(self):  # aka the update-loop method
        # for i in range(5):
        #     self.add_line_below()
        #     self.remove_line_above()
        self.board[0][0] = 2
        while True:
            pressed_key = readchar.readkey()
            if(pressed_key == readchar.key.CTRL_C or pressed_key == readchar.key.CTRL_D):
                break
            if(pressed_key == readchar.key.SPACE):
                self.swap_piece()
            if(pressed_key in self.controller_keys["move"]):
                self.move_cursor(pressed_key)

            self.dispatch_actions()
            # print(self.action_queue)


Game([5, 6]).play()
