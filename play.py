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

def print_board(board, next_line = None, steps = 1):
  os.system('cls' if os.name == 'nt' else 'clear')
  for index, line in enumerate(reversed(board)):
    print(*line, sep='')

def update_board(board):
  moved = False
  time.sleep(.3)
  for row_index, row in enumerate(board):
    for cell_index, cell in enumerate(row):
      last_empty_space = row_index
      
      if board[row_index][cell_index] != s[0]:
        if board[last_empty_space - 1][cell_index] == s[0]:
          moved = True
        while board[last_empty_space - 1][cell_index] == s[0] \
          and last_empty_space > 0:
            last_empty_space -= 1

        board[row_index][cell_index] = s[0]
        board[last_empty_space][cell_index] = cell

  if moved:print_board(board)

  matched, board = check_for_match(board)
  if matched: print_board(board)
  
  return board

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
