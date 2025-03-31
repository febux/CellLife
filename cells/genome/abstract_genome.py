from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class BaseGenome:
    """
    A class representing the base genome of a cellular automaton.

    Attributes:
        energy_capacity: An integer representing the initial energy capacity of the cell.
        neighbors_amounts_to_kill: A tuple of integers representing the number of neighbors to kill.
        neighbors_to_reproduction: An integer representing the number of neighbors needed for reproduction.
        energy_boost_rate: A float representing the rate of energy boost.
        cell_boost_rate: A float representing the rate of cell boost.
        energy_consumption_rate: A float representing the rate of energy consumption.
        poison_rate: A float representing the rate of poison.
    """
    energy_capacity: int = 0

    neighbors_amounts_to_kill: Optional[Tuple[int, ...]] = None
    neighbors_to_reproduction: Optional[int] = None

    energy_boost_rate: Optional[float] = None
    cell_boost_rate: Optional[float] = None
    energy_consumption_rate: Optional[float] = None
    poison_rate: Optional[float] = None

    mutation_chance: Optional[float] = None
    mutated_cell: Optional[str] = None
