import os
import time
import re
from enum import IntEnum

class Side(IntEnum):
    LEFT = 0
    RIGHT = 1


def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')
