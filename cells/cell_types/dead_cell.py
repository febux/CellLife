from typing import Dict

from cells.cell_types.abstract_cell import BaseCell, TCell
from constants import Color
from constants.constants import ENERGY_ITERATION_VALUE
from constants.type_alias import Matrix, Vector


class DeadCell(BaseCell):
    energy_value = 10

    def __init__(self, x: int, y: int, color: Color = Color.GRAY) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 50

    def check_energy_cells(self, cells: Matrix = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellTypeCatalog

        if self.energy_capacity <= 0:
            return CellTypeCatalog.EmptyCell.class_(self.x, self.y)
        else:
            self.energy_capacity -= ENERGY_ITERATION_VALUE
            return self

    def cell_iteration_behavior(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellTypeCatalog

        for neighbor_type, neighbor_type_amount in neighbors.items():
            if neighbor_type in CellTypeCatalog.get_predators():
                self.energy_capacity -= self.energy_value
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return False
