import random
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Dict

from cells.genome.abstract_genome import BaseGenome
from constants import Color, CELL_SIZE
from constants.type_alias import TCell


class BaseMutationMixin:
    @classmethod
    def try_cell_mutation(cls, x: int, y: int):
        """
        Attempt to mutate a cell based on its genome's mutation chance.

        This method checks if the cell's genome has a mutation chance and a specified
        mutated cell type. If so, it attempts to create either the original cell type
        or the mutated cell type based on the mutation chance.

        Args:
            cls: The class on which this method is called.
            x (int): The x-coordinate for the cell.
            y (int): The y-coordinate for the cell.

        Returns:
            An instance of either the original cell type or the mutated cell type,
            based on the mutation chance. If mutation is not possible or fails,
            it returns an instance of the original cell type.
        """
        from cells.cell_type_catalog import CellTypeCatalog

        if cls.genome.mutation_chance and cls.genome.mutated_cell:
            mutation_chance = cls.genome.mutation_chance * 100
            return random.choices(
                [cls(x, y), CellTypeCatalog[cls.genome.mutated_cell].class_(x, y)],
                weights=(100, mutation_chance)
            )[0]
        return cls(x, y)


class BaseCell(ABC):
    """
    Abstract class representing a cell in a Conway's Game of Life simulation.

    Attributes:
        x (int): x-coordinate of the cell
        y (int): y-coordinate of the cell
        color (Color): color of the cell
        size (int): size of the cell type
        energy_value (int): current energy value of the cell type
        energy_capacity (int): maximum energy capacity of the cell
        neighbor_positions (Tuple[Tuple[int, int], ...]): array of neighbors' positions over the cell type
        genome (Optional[BaseGenome]): the genome of the cell

    """

    neighbor_positions: Tuple[Tuple[int, int], ...] = (
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1),
    )
    size: int = CELL_SIZE
    energy_value: int = 0

    genome: Optional[BaseGenome] = None

    __slots__ = ("x", "y", "color", "energy_capacity")

    def __init__(self, x: int, y: int, color: Color = None):
        """
        Initialize a new Cell instance.

        Args:
            x (int): x-coordinate of the cell
            y (int): y-coordinate of the cell
            color (Color): color of the cell

        """
        self.x = x
        self.y = y
        self.color = color
        self.energy_capacity: int = 0

    def check_neighbors(self, cells: List[List[TCell]]) -> Dict[str, List[TCell]]:
        """
        Check the neighbors of the current cell.

        Args:
            cells (List[List[TCell]]): 2D list of cells

        Returns:
            Dict[str, List[TCell]]: a dictionary containing the types of neighbors and their corresponding cells

        """
        neighbors_types__map: Dict[str, List[TCell]] = dict()
        for neighbor_position in self.neighbor_positions:
            cell = cells[(self.x + neighbor_position[0]) % len(cells)][(self.y + neighbor_position[1]) % len(cells[0])]
            if type(cell).__name__ not in neighbors_types__map:
                neighbors_types__map[type(cell).__name__] = [cell]
            else:
                neighbors_types__map[type(cell).__name__].append(cell)

        return neighbors_types__map

    @abstractmethod
    def check_energy_cells(self, cells: List[List[TCell]]) -> int:
        """
        Check the energy of the current cell.

        Args:
            cells (List[List[TCell]]): 2D list of cells

        Returns:
            int: the energy value of the current cell which was calculated based on the current position and neighbors

        """
        raise NotImplementedError

    @abstractmethod
    def recalculate_cell_energy(self, cells: List[List[TCell]]) -> TCell:
        """
        Recalculate the energy of the current cell.

        Args:
            cells (List[List[TCell]]): 2D list of cells

        Returns:
            TCell: the updated cell with the recalculated energy

        """
        raise NotImplementedError

    @abstractmethod
    def cell_iteration_behavior(self, neighbors: Dict[str, List[TCell]], cells: List[List[TCell]]) -> TCell:
        ...

    @property
    @abstractmethod
    def cell_liveness(self) -> bool:
        """
        Check if the current cell is alive.

        Returns:
            bool: True if the current cell is alive, False otherwise

        """
        raise NotImplementedError
