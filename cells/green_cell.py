from typing import List

from cells.abstract_cell import Cell, TCell
from cells.dead_cell import DeadCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.genome.green_cell__genome import GreenCellGenome
from constants.constants import Color


class GreenCell(Cell):
    energy_value = 20
    genome = GreenCellGenome

    def __init__(self, x: int, y: int, color: Color = Color.GREEN) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 200

    def check_energy_cells(self, cells: List[List[TCell]]) -> int:
        energy: int = 0
        for neighbor_position in self.neighbor_positions:
            neighbor_cell = cells[
                (self.x + neighbor_position[0]) % len(cells)
                ][
                (self.y + neighbor_position[1]) % len(cells[0])
                ]
            if isinstance(neighbor_cell, EnergyCell):
                energy += self.genome.energy_boost__rate * neighbor_cell.energy_value
        return energy

    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> TCell:
        if self.energy_capacity <= 0:
            return DeadCell(self.x, self.y)
        else:
            neighbors = self.check_neighbors(cells=cells).get(type(self).__name__, [])
            if len(neighbors) not in self.genome.neighbors_amounts_to_kill:
                return EmptyCell(self.x, self.y)

            if energy_value := self.check_energy_cells(cells=cells):
                self.energy_capacity += energy_value

            self.energy_capacity -= self.genome.energy_consumption__rate * self.energy_value
            return self

    @property
    def cell_liveness(self) -> bool:
        return True
