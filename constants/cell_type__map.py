from cells.dead_red_cell import DeadRedCell
from cells.dead_cell import DeadCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.green_cell import GreenCell
from cells.purple_cell import PurpleCell
from cells.red_cell import RedCell
from cells.yellow_cell import YellowCell


CELL_TYPE__MAP = {
    'EmptyCell': EmptyCell,
    'EnergyCell': EnergyCell,
    'GreenCell': GreenCell,
    'RedCell': RedCell,
    'PurpleCell': PurpleCell,
    'YellowCell': YellowCell,
    'DeadCell': DeadCell,
    'DeadRedCell': DeadRedCell,
}
