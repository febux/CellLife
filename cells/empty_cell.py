from typing import List

from cells.abstract_cell import Cell, TCell
from constants.constants import Color


class EmptyCell(Cell):
    def __init__(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 0

    def check_energy_cells(self, cells: List[List[TCell]] = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> None:
        pass

    @property
    def cell_liveness(self) -> bool:
        return False
