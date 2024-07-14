from typing import List, Dict

from cells.abstract_cell import Cell, TCell
from constants import Color
from constants.constants import ENERGY_ITERATION_VALUE
from constants.type_alias import Matrix, Vector


class DeadRedCell(Cell):
    energy_value = 10

    def __init__(self, x: int, y: int, color: Color = Color.BLUE) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 30

    def check_energy_cells(self, cells: Matrix = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellType

        if self.energy_capacity <= 0:
            return CellType.EmptyCell.class_(self.x, self.y)
        else:
            self.energy_capacity -= ENERGY_ITERATION_VALUE
            return self

    def cell_iteration(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return False
