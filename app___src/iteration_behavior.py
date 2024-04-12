import random
from typing import List

from cells.abstract_cell import TCell
from cells.dead_red_cell import DeadRedCell
from cells.empty_cell import EmptyCell
from cells.green_cell import GreenCell
from cells.purple_cell import PurpleCell
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
                if neighbor_type_cls is GreenCell and len(neighbors) == GreenCell.genome.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return random.choices([GreenCell(x, y), YellowCell(x, y)], weights=(100, 5))[0]
                elif neighbor_type_cls is YellowCell and len(neighbors) == YellowCell.genome.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return YellowCell(x, y)
                elif neighbor_type_cls is RedCell and len(neighbors) == RedCell.genome.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return random.choices([RedCell(x, y), PurpleCell(x, y)], weights=(100, 4))[0]
                elif neighbor_type_cls is PurpleCell and len(neighbors) == PurpleCell.genome.neighbors_to_reproduction:
                    x, y = watched_cell.x, watched_cell.y
                    return PurpleCell(x, y)
            return watched_cell
        case 'EnergyCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is GreenCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * GreenCell.genome.energy_boost__rate
                if neighbor_type_cls is YellowCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * YellowCell.genome.energy_boost__rate
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * RedCell.genome.energy_boost__rate
                if neighbor_type_cls is PurpleCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * PurpleCell.genome.energy_boost__rate
            return watched_cell.recalculate_cell_energy(cells)
        case 'GreenCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is DeadRedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * GreenCell.genome.poison_rate
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * RedCell.genome.cell_boost__rate
                if neighbor_type_cls is PurpleCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * PurpleCell.genome.cell_boost__rate
            return watched_cell.recalculate_cell_energy(cells)
        case 'YellowCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is DeadRedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * YellowCell.genome.poison_rate
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * RedCell.genome.cell_boost__rate
                if neighbor_type_cls is PurpleCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * PurpleCell.genome.cell_boost__rate
            return watched_cell.recalculate_cell_energy(cells)
        case 'RedCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is DeadRedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * RedCell.genome.poison_rate
            return watched_cell.recalculate_cell_energy(cells)
        case 'PurpleCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is DeadRedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value * PurpleCell.genome.poison_rate
            return watched_cell.recalculate_cell_energy(cells)
        case 'DeadRedCell':
            return watched_cell.recalculate_cell_energy(cells)
        case 'DeadCell':
            for neighbor_type, neighbor_type_amount in neighbors_by_types.items():
                neighbor_type_cls = CELL_TYPE__MAP[neighbor_type]
                if neighbor_type_cls is RedCell:
                    watched_cell.energy_capacity -= watched_cell.energy_value
            return watched_cell.recalculate_cell_energy(cells)
        case _:
            return EmptyCell(watched_cell.x, watched_cell.y)
