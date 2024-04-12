from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class GreenCellGenome(BaseGenome):
    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3
    energy_boost__rate: float = 1.0
    energy_consumption__rate: float = 0.5
    poison_rate: float = 1.5
