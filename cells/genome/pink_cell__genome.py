from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class PinkCellGenome(BaseGenome):
    energy_capacity: int = 400

    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3

    energy_boost_rate: float = 1.25
    cell_boost_rate: float = 4.5
    energy_consumption_rate: float = 0.5
    poison_rate: float = 1.0
