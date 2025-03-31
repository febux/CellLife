from typing import Dict

from cells.cell_types.abstract_cell import BaseCell
from constants import Color
from constants.constants import ENERGY_ITERATION_VALUE
from constants.type_alias import Matrix, Vector, TCell


class DeadRedCell(BaseCell):
    energy_value = 10

    def __init__(self, x: int, y: int, color: Color = Color.BLUE) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 30

    def check_energy_cells(self, cells: Matrix = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: Matrix) -> TCell:
        from cells.cell_type_catalog import CellTypeCatalog

        if self.energy_capacity <= 0:
            return CellTypeCatalog.EmptyCell.class_(self.x, self.y)
        else:
            self.energy_capacity -= ENERGY_ITERATION_VALUE
            return self

    def cell_iteration_behavior(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return False
