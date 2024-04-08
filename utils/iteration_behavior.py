import random
from typing import List

from cells.abstract_cell import TCell
from cells.blue_cell import BlueCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.green_cell import GreenCell
from cells.red_cell import RedCell
from cells.yellow_cell import YellowCell
from constants.cell_type__map import CELL_TYPE__MAP


def iteration_behavior(watched_cell: TCell, cells: List[List[TCell]]) -> TCell:
    """
    This method is used to iterate over the cells in the array and return calculated behavior of each cell

    Parameters:
    watched_cell (TCell): The current cell to iterate over in the iteration
    cells (List[List[TCell]]): The cells array to iterate over in the iteration

    Returns:
    TCell: The calculated behavior of cell to iterate over in the iteration
    """
    neighbors_by_types = watched_cell.check_neighbors(cells=cells)

    watched_cell_type_name = type(watched_cell).__name__

    match watched_cell_type_name:
        case 'EmptyCell':
            for neighbor_type, neighbors in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is GreenCell and len(neighbors) == neighbor_type_cls.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return random.choices([GreenCell(x, y), YellowCell(x, y)], weights=(100, 5))[0]
                elif neighbor_type_cls is YellowCell and len(neighbors) == neighbor_type_cls.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return YellowCell(x, y)
                elif neighbor_type_cls is RedCell and len(neighbors) == neighbor_type_cls.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return RedCell(x, y)
            return watched_cell
        case 'EnergyCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is GreenCell or neighbor_type_cls is YellowCell:
                    watched_cell.energy_capacity -= EnergyCell.energy_value
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= EnergyCell.energy_value / 2
            return watched_cell.recalculate_cell_energy(cells)
        case 'GreenCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is BlueCell:
                    watched_cell.energy_capacity -= BlueCell.energy_value
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= GreenCell.energy_value
            return watched_cell.recalculate_cell_energy(cells)
        case 'YellowCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is BlueCell:
                    watched_cell.energy_capacity -= BlueCell.energy_value
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= YellowCell.energy_value
            return watched_cell.recalculate_cell_energy(cells)
        case 'RedCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is BlueCell:
                    watched_cell.energy_capacity -= BlueCell.energy_value * 2
            return watched_cell.recalculate_cell_energy(cells)
        case 'BlueCell':
            return watched_cell.recalculate_cell_energy(cells)
        case _:
            return EmptyCell(watched_cell.x, watched_cell.y)
