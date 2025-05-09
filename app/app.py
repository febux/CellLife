import sys

import pygame as pg
from pygame import Surface, SurfaceType, time

from app.cells_generator import field_cells_generator
from cells.cell_types.abstract_cell import TCell
from constants.colors import Color
from constants.constants import CELL_SIZE, FPS
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
        self.cells: Matrix = []

        self.clock = time.Clock()
        self.clock.tick(FPS)

        self.start_game()

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

    def recalculate_cells__iteration(self) -> None:
        """
        The recalculate_cells__iteration method calculates the next generation of cells.

        Returns:
            Matrix: The next generation of cells.
        """
        self.cells = [
            [self.iteration_behavior(self.cells[x][y]) for y in range(0, self.app_width // self.cell_size)]
            for x in range(0, self.app_height // self.cell_size)
        ]

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

        return watched_cell.cell_iteration_behavior(neighbors_by_types, cells=self.cells)

    def event_listener(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_ESCAPE:
                        self.exit_game()
                    case pg.K_r:
                        self.start_game()

    def run(self) -> None:
        """
        The run method is the game loop that runs the simulation.
        """
        while True:
            self.root.fill(Color.WHITE.value)

            self.event_listener()

            self.draw_cells()

            pg.display.update()

            self.recalculate_cells__iteration()

            self.iterations += 1

    def exit_game(self):
        print(f"iterations={self.iterations}")
        pg.quit()
        sys.exit(0)

    def start_game(self):
        print(f"iterations={self.iterations}")
        self.iterations = 0
        self.cells: Matrix = field_cells_generator(self.root, cell_size=self.cell_size)
