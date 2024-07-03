from typing import List, Dict

from cells.abstract_cell import Cell, TCell
from cells.genome.pink_cell__genome import PinkCellGenome
from constants import Color


class PinkCell(Cell):
    energy_value = 20
    genome = PinkCellGenome

    def __init__(self, x: int, y: int, color: Color = Color.PINK) -> None:
        super().__init__(x, y, color)
        self.energy_capacity = 400

    def check_energy_cells(self, cells: List[List[TCell]]) -> int:
        from cells.cell_type_enum import CellType

        energy: int = 0
        for neighbor_position in self.neighbor_positions:
            neighbor_cell = cells[
                (self.x + neighbor_position[0]) % len(cells)
                ][
                (self.y + neighbor_position[1]) % len(cells[0])
                ]
            neighbor_type = type(neighbor_cell).__name__
            if neighbor_type in CellType.get_herbivores():
                energy += neighbor_cell.energy_value
            elif neighbor_type in CellType.get_predators():
                energy += neighbor_cell.energy_value
            elif neighbor_type == CellType.DeadCell.value:
                energy += neighbor_cell.energy_value
            elif neighbor_type == CellType.EnergyCell.value:
                energy += self.genome.energy_boost__rate * neighbor_cell.energy_value
        return energy

    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> TCell:
        from cells.cell_type_enum import CellType

        if self.energy_capacity <= 0:
            return CellType.DeadCell.class_(self.x, self.y)
        else:
            neighbors = self.check_neighbors(cells=cells).get(type(self).__name__, [])
            if len(neighbors) not in self.genome.neighbors_amounts_to_kill:
                return CellType.EmptyCell.class_(self.x, self.y)

            if energy_value := self.check_energy_cells(cells=cells):
                self.energy_capacity += energy_value

            self.energy_capacity -= self.genome.energy_consumption__rate * self.energy_value
            return self

    def cell_iteration(self, neighbors: Dict[str, List[TCell]], cells: List[List[TCell]]) -> TCell:
        from cells.cell_type_enum import CellType

        for neighbor_type, neighbor_type_amount in neighbors.items():
            if neighbor_type in CellType.get_poison_cells():
                self.energy_capacity -= self.energy_value * self.genome.poison_rate
        return self.recalculate_cell_energy(cells)

    @property
    def cell_liveness(self) -> bool:
        return True
