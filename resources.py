from enum import IntEnum

class BlockIndex(IntEnum):
    EMPTY = 0
    STAR = 1
    TRIANGLE = 2
    HEART = 3
    CIRCLE = 4
    DIAMOND = 5

empty_block = "   "
star_block = "\033[103m\033[97m ✲ \033[0m"
triangle_block = "\033[104m\033[97m ▲ \033[0m"
heart_block = "\033[101m\033[97m ♥ \033[0m"
circle_block = "\033[102m\033[97m ● \033[0m"
diamond_block = "\033[105m\033[97m ◆ \033[0m"

blocks = [
    empty_block,
    star_block,
    triangle_block,
    heart_block,
    circle_block,
    diamond_block
]

colors = [
    "\033[0m",
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[97m"
]
letters = [
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
]

title = """
 a.---.z b.----.zc.----.z d.-.   .-.e.-.d.-. .-.z  c.--.z  b.-.z
a(_   _)zb| (_z  c| ()  )zd|  `.'  |e| |d|  `| |z c/ () \z b| |z
  a| |z  b| (__z c| .-. \zd| |\ /| |e| |d| |\  |zc/  /\  \zb| `--.z
  a`-'z  b`----'zc`-' `-'zd`-' ` `-'e`-'d`-' `-'zc`-'  `-'zb`----'z
        c.--.z  e.---.z  a.---.z  d.--.z   b.---.z a.-. .-.z
       c/ () \ze(_   _)za(_   _)zd/ () \z b/  ___)za| |/ /z
      c/  /\  \z e| |z    a| |z d/  /\  \zb\     )za| |\ \z
      c`-'  `-'z e`-'z    a`-'z d`-'  `-'z b`---'z a`-' `-'z

           \033[5m=== PRESS ANY KEY TO START ===\033[0m
"""


def generate_title():
    colored_title = title
    for i, letter in enumerate(letters):
        colored_title = colored_title.replace(letter, colors[i])
    return colored_title
