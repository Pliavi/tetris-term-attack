import time, os, random


def add_line(board):
  line = [s[random.randint(1,5)] for x in range(len(board[0]))]
  board.insert(0, line)
  del board[-1]
  return board

def new_board(pattern):
  new_board = [[s[0] for x in range(6)] for y in range(5)]
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
  print('moved: ', piece[x],',', piece[y], ' to ', 'left' if side == -1 else 'right', sep="")
  return board

def check_for_match(board):
  changed = False
  for row_i, row in enumerate(board):
    for col_i, cell in enumerate(row):
      if cell != s[0]:
        h_matching = 1
        v_matching = 1
        matches = [[row_i, col_i]]
        while col_i + h_matching < len(board[row_i]) and board[row_i][col_i + h_matching] == cell:
          matches.append([row_i, col_i + h_matching])
          h_matching += 1
        while row_i + v_matching < len(board) and board[row_i + v_matching][col_i] == cell:
          matches.append([row_i + v_matching, col_i])
          v_matching += 1
        if(h_matching > 2 or v_matching > 2):
          for match in matches:
            board[match[0]][match[1]] = s[0]
          board = update_board(board)
          changed = True
  return changed, board

def auto_game():
  board = new_board([
    [s[0], s[0], s[0], s[0], s[1], s[0]],
    [s[0], s[3], s[1], s[0], s[5], s[1]],
    [s[0], s[3], s[3], s[5], s[5], s[1]],
    [s[0], s[2], s[4], s[1], s[2], s[2]]
  ])
  #[row, col]
  move_piece(board, [0,1], 1)
  move_piece(board, [0,2], 1)
  move_piece(board, [1,4], -1)
  move_piece(board, [1,3], -1)
  move_piece(board, [1,2], -1)
  move_piece(board, [1,1], -1)
  move_piece(board, [0,0], 1)
  move_piece(board, [0,1], 1)
  move_piece(board, [1,5], -1)
  move_piece(board, [1,4], -1)

os.system('cls' if os.name == 'nt' else 'clear')
auto_game()
