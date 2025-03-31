from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class GreenCellGenome(BaseGenome):
    energy_capacity: int = 150

    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3

    energy_boost_rate: float = 1.0
    energy_consumption_rate: float = 0.7
    poison_rate: float = 1.5

    mutation_chance = 0.09
    mutated_cell = "YellowCell"
