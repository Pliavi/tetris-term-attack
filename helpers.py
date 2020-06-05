import os
import time
import re


def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')


def update_screen(board, cursor=[0, 0]):
    clear_screen()
    for y_i, y in enumerate(reversed(board)):
        for x_i, x in enumerate(y):
            # print(y_i)
            if(cursor[0] == (len(board)-y_i-1) and cursor[1] == x_i):
                x = "\033[5m" + x.replace(" ", "[", 1) + "\033[0m"
            elif(cursor[0] == (len(board)-y_i-1) and cursor[1] + 1 == x_i):
                x = "\033[5m" + re.sub(r" [^ ]*$", "]", x) + "\033[0m"
            print(x, sep='', end="")

        print()
