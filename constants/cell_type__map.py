from cells.blue_cell import BlueCell
from cells.empty_cell import EmptyCell
from cells.energy_cell import EnergyCell
from cells.green_cell import GreenCell
from cells.red_cell import RedCell
from cells.yellow_cell import YellowCell


CELL_TYPE__MAP = {
    'EmptyCell': EmptyCell,
    'EnergyCell': EnergyCell,
    'GreenCell': GreenCell,
    'RedCell': RedCell,
    'YellowCell': YellowCell,
    'BlueCell': BlueCell,
}
