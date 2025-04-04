from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class YellowCellGenome(BaseGenome):
    energy_capacity: int = 300

    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3

    energy_boost_rate: float = 1.8
    energy_consumption_rate: float = 0.7
    poison_rate: float = 1.2

    mutation_chance = 0.07
    mutated_cell = "OrangeCell"
