import random
from dataclasses import dataclass
from typing import List

import pygame as pg
from pygame import Surface, SurfaceType
from pygame.locals import QUIT

from cells.abstract_cell import TCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.green_cell import GreenCell
from cells.red_cell import RedCell
from constants.constants import CELL_SIZE, Color
from utils.iteration_behavior import iteration_behavior


@dataclass
class Population:
    """
    the Population class is used to store and manage the probabilities
    of each cell type in the simulation, allowing the simulation
    to accurately reflect the behavior of real cells in a population.
    """
    def __init__(
        self,
        empty_cell__population,
        energy_cells__population,
        green_cells__population,
        red_cells__population,
    ):
        self.empty_cell__population = empty_cell__population
        self.energy_cells__population = energy_cells__population
        self.green_cells__population = green_cells__population
        self.red_cells__population = red_cells__population

    def to_tuple(self):
        return (
            self.empty_cell__population,
            self.energy_cells__population,
            self.green_cells__population,
            self.red_cells__population,
        )


class App:
    """
    The App class is the main game loop that runs the simulation.
    """

    iterations = 0

    def __init__(self, width: int, height: int, root: Surface | SurfaceType, *, cell_size: int = CELL_SIZE) -> None:
        """
        The __init__ method initializes the game window, sets up the simulation, and initializes the population.

        Args:
            width (int): The width of the game window.
            height (int): The height of the game window.
            root (Surface | SurfaceType): The game window.
            cell_size (int, optional): The size of each cell. Defaults to CELL_SIZE.
        """
        self.root = root
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells: List[List[TCell]] = [
            [
                random.choices(
                    (EmptyCell(x, y), EnergyCell(x, y), GreenCell(x, y), RedCell(x, y)),
                    weights=Population(
                        empty_cell__population=300,
                        energy_cells__population=10,
                        green_cells__population=20,
                        red_cells__population=10,
                    ).to_tuple(),
                )[0]
                for y in range(self.root.get_height() // CELL_SIZE)
            ]
            for x in range(self.root.get_width() // CELL_SIZE)
        ]

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
        temp_res_cells: List[List[TCell]] = [[EmptyCell(x, y) for y in range(len(self.cells[0]))]
                                             for x in range(len(self.cells))]
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                temp_res_cells[x][y] = iteration_behavior(self.cells[x][y], cells=self.cells)
        return temp_res_cells

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