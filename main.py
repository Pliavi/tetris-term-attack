import random
from resources import *
from helpers import *
import readchar
from typing import List
from enum import IntEnum


class Axis(IntEnum):
    COL = 1
    ROW = 0


class Game(object):
    """ 
        frame_stack: is the diff stack in the board that 
                     is dispatched each "frame"
    """
    board: List[List[int]] = []
    board_size: List[int] = [0, 0]
    cursor_pos: List[int] = [0, 0]
    ticks: int = 0
    game_finished: bool = False
    frame_stack: List[List[int]] = None

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
        for row_index, row in enumerate(self.board):
            if callback_to_rows:
                callback_to_rows(row_index, row)
            for cell_index, cell in enumerate(self.board[row_index]):
                if callback_to_cells:
                    callback_to_cells(cell_index, cell, row_index, row)

    def do_drops(self):
        dropped = False
        def check_drops(cell_index, cell, row_index, line):
            is_first_row = row_index == 0
            if not(is_first_row) and board[row_index][cell_index] != BlockIndex.EMPTY:
                next_possibly_empty_row = row_index
                while True:
                    next_possibly_empty_row -= 1
                    if self.board[next_possibly_empty_row][cell_index] != BlockIndex.EMPTY:
                        self.frame_stack.append([
                            [row_index, cell_index, BlockIndex.EMPTY],
                            [next_possibly_empty_row, cell_index, cell]
                        ])
                        break
            # self.frame_stack = [row_index][cell_index] = BlockIndex.EMPTY
            # self.frame_stack = [last_empty_row][cell_index] = cell
                    
        self.run_in_board()

    def move_piece(self):
        pass

    def move_cursor(self):
        pass

    def play(self):  # aka the update-loop method
        pass


game = Game()
