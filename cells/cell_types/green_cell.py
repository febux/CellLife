import random
from typing import Dict

from cells.abstract_cell import Cell, TCell
from cells.genome.green_cell__genome import GreenCellGenome
from constants import Color
from constants.type_alias import Matrix, Vector


class GreenCell(Cell):
    energy_value = 20
    genome = GreenCellGenome

    def __init__(self, x: int, y: int, color: Color = Color.GREEN) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = self.genome.energy_capacity

    @classmethod
    def try_cell_mutation(cls, x: int, y: int):
        from cells.cell_type_enum import CellType

        return random.choices([cls(x, y), CellType.YellowCell.class_(x, y)], weights=(100, 5))[0]

    def check_energy_cells(self, cells: Matrix) -> int:
        from cells.cell_type_enum import CellType

        energy: int = 0
        for neighbor_position in self.neighbor_positions:
            neighbor_cell = cells[
                (self.x + neighbor_position[0]) % len(cells)
                ][
                (self.y + neighbor_position[1]) % len(cells[0])
                ]
            neighbor_type = type(neighbor_cell).__name__
            if neighbor_type == CellType.EnergyCell.value:
                energy += self.genome.energy_boost_rate * neighbor_cell.energy_value
        return energy

    def recalculate_cell_energy(self, cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellType

        if self.energy_capacity <= 0:
            return CellType.DeadCell.class_(self.x, self.y)
        else:
            neighbors = self.check_neighbors(cells=cells).get(type(self).__name__, [])
            if len(neighbors) not in self.genome.neighbors_amounts_to_kill:
                return CellType.EmptyCell.class_(self.x, self.y)

            if energy_value := self.check_energy_cells(cells=cells):
                self.energy_capacity += energy_value

            self.energy_capacity -= self.genome.energy_consumption_rate * self.energy_value
            return self

    def cell_iteration(self, neighbors: Dict[str, Vector], cells: Matrix) -> TCell:
        from cells.cell_type_enum import CellType

        for neighbor_type, neighbor_type_amount in neighbors.items():
            neighbor_type_cls = CellType(neighbor_type).class_
            if neighbor_type in CellType.get_poison_cells():
                self.energy_capacity -= self.energy_value * self.genome.poison_rate
            elif neighbor_type in CellType.get_predators():
                self.energy_capacity -= self.energy_value * neighbor_type_cls.genome.cell_boost_rate
            elif neighbor_type in CellType.get_super_predators():
                self.energy_capacity -= self.energy_value * neighbor_type_cls.genome.cell_boost_rate
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return True
