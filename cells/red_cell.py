from typing import List

from cells.abstract_cell import Cell, TCell
from cells.blue_cell import BlueCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.green_cell import GreenCell
from cells.yellow_cell import YellowCell
from constants.constants import Color


class RedCell(Cell):
    neighbors_to_reproduction = 3
    genome = (1, 2, 4)
    energy_value = 30
    energy_boost__rate: float = 0.25
    energy_consumption__rate: float = 1.0

    def __init__(self, x: int, y: int, color: Color = Color.RED) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 300

    def check_energy_cells(self, cells: List[List[TCell]]) -> int:
        energy: int = 0
        for neighbor_position in self.neighbor_positions:
            neighbor_cell = cells[
                (self.x + neighbor_position[0]) % len(cells)
                ][
                (self.y + neighbor_position[1]) % len(cells[0])
                ]
            if type(neighbor_cell) is GreenCell or type(neighbor_cell) is YellowCell:
                energy += neighbor_cell.energy_value
            elif type(neighbor_cell) is EnergyCell:
                energy += self.energy_boost__rate * neighbor_cell.energy_value
        return energy

    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> TCell:
        if self.energy_capacity <= 0:
            return BlueCell(self.x, self.y)
        else:
            neighbors = self.check_neighbors(cells=cells).get(type(self).__name__, [])
            if len(neighbors) not in self.genome:
                return EmptyCell(self.x, self.y)

            if energy_value := self.check_energy_cells(cells=cells):
                self.energy_capacity += energy_value

            self.energy_capacity -= self.energy_consumption__rate * self.energy_value
            return self

    @property
    def cell_liveness(self) -> bool:
        return True
