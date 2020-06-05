import random
from resources import *
from helpers import *
import readchar


def add_line_below(board):
    line_size = len(board[0])
    line = [blocks[random.randint(1, 5)] for i in range(line_size)]
    board.insert(0, line)

    return board


def remove_line_above(board):
    del board[-1]

    return board


def new_board(pattern=None):
    new_board = [[white_block for x in range(6)] for y in range(10)]

    if pattern:
        for index, line in enumerate(reversed(pattern)):
            new_board[index] = line

    return new_board


def run_in_board(board, callback):
    need_screen_update = False
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if need_screen_update:
                board = callback(
                    board, row, row_index, cell, cell_index)[1]
            else:
                need_screen_update, board = callback(
                    board, row, row_index, cell, cell_index)

    return need_screen_update, board


def update_board(board):
    checks = [check_for_drop, check_for_match]

    for check_function in checks:
        need_screen_update, board = run_in_board(board, check_function)
        if need_screen_update:
            update_screen(board)

    return board


def check_for_drop(board, row, row_index, cell, cell_index):
    moved = False
    last_empty_space = row_index
    if board[row_index][cell_index] != white_block:
        def has_white_space_below(
        ): return board[last_empty_space - 1][cell_index] == white_block

        moved = has_white_space_below()
        while has_white_space_below() and last_empty_space > 0:
            last_empty_space -= 1

        board[row_index][cell_index] = white_block
        board[last_empty_space][cell_index] = cell

    return moved, board


def check_for_match(board, row, row_index, cell, cell_index):
    matched = False
    if cell != white_block:
        h_matching = 1
        v_matching = 1
        matches = [[row_index, cell_index]]
        while cell_index + h_matching < len(board[row_index]) and board[row_index][cell_index + h_matching] == cell:
            matches.append([row_index, cell_index + h_matching])
            h_matching += 1
        while row_index + v_matching < len(board) and board[row_index + v_matching][cell_index] == cell:
            matches.append([row_index + v_matching, cell_index])
            v_matching += 1
        if(h_matching > 2 or v_matching > 2):
            for match in matches:
                board[match[0]][match[1]] = white_block
            board = update_board(board)
            matched = True

    return matched, board


def move_piece(board, piece, side):
    x, y = 1, 0
    if piece[x] + side >= 0 \
            and piece[x] + side < len(board[0]):
        move_to = board[piece[y]][piece[x] + side]
        board[piece[y]][piece[x] + side] = board[piece[y]][piece[x]]
        board[piece[y]][piece[x]] = move_to
    board = update_board(board)

    return board


def move_cursor(pressed_key, cursor):
    x, y = 1, 0

    if pressed_key == readchar.key.UP:
        cursor[y] += 1
    if pressed_key == readchar.key.DOWN:
        cursor[y] -= 1
    if pressed_key == readchar.key.LEFT:
        cursor[x] -= 1
    if pressed_key == readchar.key.RIGHT:
        cursor[x] += 1

    return cursor


def playable_game():
    ticks = 0
    cursor = [0, 0]
    board = new_board()
    for i in range(5):
        add_line_below(board)

    while True:
        if ticks % 20 == 0:
            board = add_line_below(board)
            board = remove_line_above(board)
        pressed_key = readchar.readkey()
        if(pressed_key == readchar.key.CTRL_C or pressed_key == readchar.key.CTRL_D):
            break
        cursor = move_cursor(pressed_key, cursor)
        update_screen(board, cursor)
        ticks += 1


clear_screen()
print("""
.----. .----. .----. .----. .----.
| ()  )| ()  )| (_  ( (__  ( (__
| .--' | .-. \| (__ .-._) ).-._) )
`-'    `-' `-'`----'`----' `----'
      .--.  .-. .-..-.  .-.
     / () \ |  `| | \ \/ /
    /  /\  \| |\  |  )  (
    `-'  `-'`-' `-'  `--'
    .-. .-..----..-.  .-.
    | |/ / | (_   \ \/ /
    | |\ \ | (__   )  (
    `-' `-'`----'  `--'
""")

clear_screen()
# auto_game()
playable_game()
