import random
from typing import List

from pygame import Surface, SurfaceType

from cells.abstract_cell import TCell
from cells.cell_type_enum import CellType
from constants.constants import POPULATION, CELL_SIZE


def field_cells_generator(root: Surface | SurfaceType, *, cell_size: int = CELL_SIZE):
    return [
        [
            random.choices(
                (
                    CellType.EmptyCell.class_(x, y),
                    CellType.EnergyCell.class_(x, y),
                    CellType.GreenCell.class_(x, y),
                    CellType.RedCell.class_(x, y)
                ),
                weights=POPULATION,
            )[0]
            for y in range(root.get_height() // cell_size)
        ]
        for x in range(root.get_width() // cell_size)
    ]


def temp_cells_generator(cells: List[List[TCell]]):
    return [[CellType.EmptyCell.class_(x, y) for y in range(len(cells[0]))] for x in range(len(cells))]
