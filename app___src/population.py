from dataclasses import dataclass


@dataclass
class Population:
    """
    the Population class is used to store and manage the probabilities
    of each cell type in the simulation, allowing the simulation
    to accurately reflect the behavior of real cells in a population.
    """
    def __init__(
        self,
        empty_cell__population,
        energy_cells__population,
        green_cells__population,
        red_cells__population,
    ):
        self.empty_cell__population = empty_cell__population
        self.energy_cells__population = energy_cells__population
        self.green_cells__population = green_cells__population
        self.red_cells__population = red_cells__population

    def to_tuple(self):
        return (
            self.empty_cell__population,
            self.energy_cells__population,
            self.green_cells__population,
            self.red_cells__population,
        )
