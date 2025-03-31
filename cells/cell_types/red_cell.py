import random
from typing import Dict

from cells.cell_types.abstract_cell import BaseCell, BaseMutationMixin
from cells.genome import RedCellGenome
from constants import Color
from constants.type_alias import Matrix, Vector, TCell


class RedCell(BaseCell, BaseMutationMixin):
    energy_value = 30
    genome = RedCellGenome

    def __init__(self, x: int, y: int, color: Color = Color.RED) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = self.genome.energy_capacity

    def check_energy_cells(self, cells: Matrix) -> int:
        from cells.cell_type_catalog import CellTypeCatalog

        energy: int = 0
        for neighbor_position in self.neighbor_positions:
            neighbor_cell = cells[
                (self.x + neighbor_position[0]) % len(cells)
                ][
                (self.y + neighbor_position[1]) % len(cells[0])
                ]
            neighbor_type = type(neighbor_cell).__name__
            if neighbor_type in CellTypeCatalog.get_herbivores():
                energy += neighbor_cell.energy_value
            elif neighbor_type == CellTypeCatalog.DeadCell.value:
                energy += neighbor_cell.energy_value
            elif neighbor_type == CellTypeCatalog.EnergyCell.value:
                energy += self.genome.energy_boost_rate * neighbor_cell.energy_value
        return energy

    def recalculate_cell_energy(self, cells: Matrix) -> TCell:
        from cells.cell_type_catalog import CellTypeCatalog

        if self.energy_capacity <= 0:
            return CellTypeCatalog.DeadRedCell.class_(self.x, self.y)
        else:
            neighbors = self.check_neighbors(cells=cells).get(type(self).__name__, [])
            if len(neighbors) not in self.genome.neighbors_amounts_to_kill:
                return CellTypeCatalog.EmptyCell.class_(self.x, self.y)

            if energy_value := self.check_energy_cells(cells=cells):
                self.energy_capacity += energy_value

            self.energy_capacity -= self.genome.energy_consumption_rate * self.energy_value
            return self

    def cell_iteration_behavior(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        from cells.cell_type_catalog import CellTypeCatalog

        for neighbor_type, neighbor_type_amount in neighbors.items():
            neighbor_type_cls = CellTypeCatalog(neighbor_type).class_
            if neighbor_type in CellTypeCatalog.get_poison_cells():
                self.energy_capacity -= self.energy_value * self.genome.poison_rate
            elif neighbor_type in CellTypeCatalog.get_super_predators():
                self.energy_capacity -= self.energy_value * neighbor_type_cls.genome.cell_boost_rate
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return True
