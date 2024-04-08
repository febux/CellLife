from typing import List

from cells.abstract_cell import Cell, TCell
from cells.empty_cell import EmptyCell
from constants.constants import Color


class EnergyCell(Cell):
    energy_value = 10

    def __init__(self, x: int, y: int, color: Color = Color.WHITE) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 10

    def check_energy_cells(self, cells: List[List[TCell]] = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> TCell:
        if self.energy_capacity <= 0:
            return EmptyCell(self.x, self.y)
        else:
            return self

    @property
    def cell_liveness(self) -> bool:
        return False
