import random

from pygame import Surface, SurfaceType

from cells.cell_type_enum import CellTypeCatalog
from constants.constants import POPULATION, CELL_SIZE
from constants.type_alias import Matrix


def field_cells_generator(root: Surface | SurfaceType, *, cell_size: int = CELL_SIZE) -> Matrix:
    """
    This function generates a 2D list of cells representing the game field.

    Parameters:
    root (Surface | SurfaceType): The root surface where the game field is displayed.
    cell_size (int): The size of each cell in the game field. Default is the value of CELL_SIZE constant.

    Returns:
    Matrix: A 2D list of cells where each cell is an instance of a subclass of TCell.

    The function uses the random.choices() function to randomly select a cell type from the list of
    possible cell types (EmptyCell, EnergyCell, GreenCell, RedCell) based on the weights defined in the
    POPULATION constant. The selected cell type is then instantiated with the corresponding x and y
    coordinates.
    """
    return [
        [
            random.choices(
                (
                    CellTypeCatalog.EmptyCell.class_(x, y),
                    CellTypeCatalog.EnergyCell.class_(x, y),
                    CellTypeCatalog.GreenCell.class_(x, y),
                    CellTypeCatalog.RedCell.class_(x, y)
                ),
                weights=POPULATION.to_tuple(),
            )[0]
            for y in range(root.get_height() // cell_size)
        ]
        for x in range(root.get_width() // cell_size)
    ]
