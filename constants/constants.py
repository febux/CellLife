from enum import Enum

CELL_SIZE = 5
WIDTH = 900
HEIGHT = 900


class Color(Enum):
    GREEN = (0, 180, 0)
    RED = (180, 0, 0)
    BLUE = (0, 0, 180)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (180, 180, 0)
