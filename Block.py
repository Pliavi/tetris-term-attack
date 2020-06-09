from enum import IntEnum, Enum
import TColors
from Helpers import Side
import re


class BlockIndex(IntEnum):
    EMPTY = 0
    HEART = 1
    CIRCLE = 2
    STAR = 3
    TRIANGLE = 4
    DIAMOND = 5


__PATTERN = "%s%s %s %s"
EMPTY = "   "
HEART =    __PATTERN % (TColors.BG_RED, TColors.FG_WHITE, "♥", TColors.RESET)
CIRCLE =   __PATTERN % (TColors.BG_GREEN, TColors.FG_WHITE, "●", TColors.RESET)
STAR =     __PATTERN % (TColors.BG_YELLOW, TColors.FG_WHITE, "✲", TColors.RESET)
TRIANGLE = __PATTERN % (TColors.BG_BLUE, TColors.FG_WHITE, "▲", TColors.RESET)
DIAMOND =  __PATTERN % (TColors.BG_PURPLE, TColors.FG_WHITE, "◆", TColors.RESET)


def by_index(block_index: BlockIndex):
    return [EMPTY, HEART, CIRCLE, STAR, TRIANGLE, DIAMOND][block_index]


def cursor_block(side: Side, block_index: BlockIndex):
    block = by_index(block_index)
    if side == Side.LEFT:
        block = block.replace(" ", "[", 1)
    else:
        block = re.sub(r" [^ ]*$", "]", block)

    return TColors.BLINK + block + TColors.RESET
