# todo: improve this file and how its interacted with...
from enum import Enum, auto

class Color(Enum):
    BLUE = auto()
    PURPLE = auto()
    RED = auto()
    CYAN = auto()
    YELLOW = auto()
    ORANGE = auto()
    GREEN = auto()
    JUNK = auto()

    @staticmethod
    def from_char(c: str) -> 'Color':
        color_map = {
            'b': Color.BLUE,
            'p': Color.PURPLE,
            'r': Color.RED,
            'c': Color.CYAN,
            'y': Color.YELLOW,
            'o': Color.ORANGE,
            'g': Color.GREEN,
            'j': Color.JUNK,
        }
        return color_map[c]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)

PINK = (255, 192, 203)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)


def get_color(color: Color):
    if color == Color.BLUE:
        return BLUE
    if color == Color.PURPLE:
        return PURPLE
    if color == Color.RED:
        return RED
    if color == Color.CYAN:
        return CYAN
    if color == Color.YELLOW:
        return YELLOW
    if color == Color.ORANGE:
        return ORANGE
    if color == Color.GREEN:
        return GREEN
    if color == Color.JUNK:
        return GRAY
