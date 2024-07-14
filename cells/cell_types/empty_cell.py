from typing import Dict

from cells.abstract_cell import Cell, TCell
from constants.colors import Color
from constants.type_alias import Matrix, Vector


class EmptyCell(Cell):
    def __init__(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        super().__init__(x, y, color)

    def check_energy_cells(self, cells: Matrix = None) -> int:
        return 0

    def recalculate_cell_energy(self, cells: Matrix) -> None:
        pass

    def cell_iteration(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellType

        for neighbor_type, neighbor_type_amount in neighbors.items():
            neighbor_type_cls = CellType(neighbor_type).class_
            if ((neighbor_type in CellType.get_mutable_cells())
                    and len(neighbor_type_amount) == neighbor_type_cls.genome.neighbors_to_reproduction):
                return neighbor_type_cls.try_cell_mutation(self.x, self.y)
            elif ((neighbor_type == CellType.get_immutable_cells())
                  and len(neighbor_type_amount) == neighbor_type_cls.genome.neighbors_to_reproduction):
                return neighbor_type_cls(self.x, self.y)
        return self

    @property
    def cell_liveness(self) -> bool:
        return False
