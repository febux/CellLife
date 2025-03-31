from typing import Tuple

from cells.genome.abstract_genome import BaseGenome


class PurpleCellGenome(BaseGenome):
    energy_capacity: int = 300

    neighbors_amounts_to_kill: Tuple[int, ...] = (1, 2, 4)
    neighbors_to_reproduction: int = 3

    energy_boost_rate: float = 0.85
    cell_boost_rate: float = 3.5
    energy_consumption_rate: float = 0.65
    poison_rate: float = 1.2

    mutation_chance = 0.06
    mutated_cell = "PinkCell"
