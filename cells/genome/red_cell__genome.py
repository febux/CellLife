from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class RedCellGenome(BaseGenome):
    energy_capacity: int = 250

    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3

    energy_boost_rate: float = 0.70
    cell_boost_rate: float = 2.5
    energy_consumption_rate: float = 0.8
    poison_rate: float = 1.5

    mutation_chance = 0.07
    mutated_cell = "PurpleCell"
