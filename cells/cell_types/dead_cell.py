from typing import List, Dict

from cells.abstract_cell import Cell, TCell
from constants import Color
from constants.constants import ENERGY_ITERATION_VALUE
from constants.type_alias import Matrix, Vector


class DeadCell(Cell):
    energy_value = 10

    def __init__(self, x: int, y: int, color: Color = Color.GRAY) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 50

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
        from cells.cell_type_enum import CellType

        for neighbor_type, neighbor_type_amount in neighbors.items():
            if neighbor_type in CellType.get_predators():
                self.energy_capacity -= self.energy_value
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return False
