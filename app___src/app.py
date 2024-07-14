from typing import List

import pygame as pg
from pygame import Surface, SurfaceType, time
from pygame.locals import QUIT

from app___src.cells_generator import field_cells_generator
from cells.abstract_cell import TCell
from constants.constants import CELL_SIZE, FPS
from constants.colors import Color
from constants.type_alias import Matrix


class App:
    """
    The App class is the main game loop that runs the simulation.
    """

    iterations = 0

    def __init__(
        self,
        root: Surface | SurfaceType,
        *,
        cell_size: int = CELL_SIZE,
    ) -> None:
        """
        The __init__ method initializes the game window, sets up the simulation, and initializes the population.

        Args:
            root (Surface | SurfaceType): The game window.
            cell_size (int, optional): The size of each cell. Defaults to CELL_SIZE.
        """
        self.root = root
        self.app_width: int = root.get_width()
        self.app_height: int = root.get_height()
        self.cell_size = cell_size
        self.cells: Matrix = field_cells_generator(root, cell_size=cell_size)
        self.clock = time.Clock()
        self.clock.tick(FPS)

    def draw_cells(self) -> None:
        """
        The draw_cells method draws the cells on the game window.
        """
        for x in range(0, self.app_height // self.cell_size):
            for y in range(0, self.app_width // self.cell_size):
                pg.draw.rect(
                    self.root,
                    self.cells[x][y].color.value,
                    [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE],
                )

    def recalculate_cells__iteration(self) -> Matrix:
        """
        The recalculate_cells__iteration method calculates the next generation of cells.

        Returns:
            Matrix: The next generation of cells.
        """
        temp_res_cells: Matrix = [
            [self.iteration_behavior(self.cells[x][y]) for y in range(0, self.app_width // self.cell_size)]
            for x in range(0, self.app_height // self.cell_size)
        ]
        return temp_res_cells

    def iteration_behavior(self, watched_cell: TCell) -> TCell:
        """
        This method is used to iterate over the cells in the array and return calculated behavior of each cell

        Parameters:
        watched_cell (TCell): The current cell to iterate over in the iteration
        cells (Matrix): The cells array to iterate over in the iteration

        Returns:
        TCell: The calculated behavior of cell to iterate over in the iteration
        """
        neighbors_by_types = watched_cell.check_neighbors(cells=self.cells)

        return watched_cell.cell_iteration(neighbors_by_types, cells=self.cells)

    def run(self) -> None:
        """
        The run method is the game loop that runs the simulation.
        """
        while True:
            self.root.fill(Color.WHITE.value)
            for i in pg.event.get():
                if i.type == QUIT:
                    quit()

            self.draw_cells()

            pg.display.update()

            self.cells = self.recalculate_cells__iteration()

            self.iterations += 1
