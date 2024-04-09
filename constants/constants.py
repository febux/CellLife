from enum import Enum

from constants.population import Population

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
    ORANGE = (255, 165, 0)
    PURPLE = (180, 0, 180)
    FUCHSIA = (153, 50, 168)
    GRAY = (128, 128, 128)
    PINK = (255, 192, 203)


population = Population(
    empty_cell__population=300,
    energy_cells__population=10,
    green_cells__population=20,
    red_cells__population=15,
).to_tuple()

