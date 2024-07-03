from typing import List

import pygame as pg
from pygame import Surface, SurfaceType, time
from pygame.locals import QUIT

from app___src.cells_generator import field_cells_generator, temp_cells_generator
from cells.abstract_cell import TCell
from constants.constants import CELL_SIZE, FPS
from constants.colors import Color


class App:
    """
    The App class is the main game loop that runs the simulation.
    """

    iterations = 0

    def __init__(self, root: Surface | SurfaceType, *, cell_size: int = CELL_SIZE) -> None:
        """
        The __init__ method initializes the game window, sets up the simulation, and initializes the population.

        Args:
            root (Surface | SurfaceType): The game window.
            cell_size (int, optional): The size of each cell. Defaults to CELL_SIZE.
        """
        self.root = root
        self.cell_size = cell_size
        self.cells: List[List[TCell]] = field_cells_generator(root, cell_size=cell_size)
        self.clock = time.Clock()
        self.clock.tick(FPS)

    def draw_cells(self) -> None:
        """
        The draw_cells method draws the cells on the game window.
        """
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells[x])):
                pg.draw.rect(
                    self.root,
                    self.cells[x][y].color.value,
                    [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE],
                )

    def recalculate_cells__iteration(self) -> List[List[TCell]]:
        """
        The recalculate_cells__iteration method calculates the next generation of cells.

        Returns:
            List[List[TCell]]: The next generation of cells.
        """
        temp_res_cells: List[List[TCell]] = temp_cells_generator(self.cells)
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                temp_res_cells[x][y] = self.iteration_behavior(self.cells[x][y])
        return temp_res_cells

    def iteration_behavior(self, watched_cell: TCell) -> TCell:
        """
        This method is used to iterate over the cells in the array and return calculated behavior of each cell

        Parameters:
        watched_cell (TCell): The current cell to iterate over in the iteration
        cells (List[List[TCell]]): The cells array to iterate over in the iteration

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
