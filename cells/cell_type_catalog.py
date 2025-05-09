from enum import Enum
import importlib
from typing import Type

from constants.type_alias import CellArray, TCell


class CellTypeCatalog(Enum):
    """
    An enumeration of cell types used in the simulation.

    This class defines various cell types and provides methods to categorize and retrieve
    different groups of cells based on their properties and behaviors.

    Attributes:
        EmptyCell (str): Represents an empty cell.
        EnergyCell (str): Represents a cell containing energy.
        GreenCell (str): Represents a green cell (typically a plant or producer).
        RedCell (str): Represents a red cell (typically a predator).
        PurpleCell (str): Represents a purple cell (typically a predator).
        YellowCell (str): Represents a yellow cell (typically an herbivore).
        DeadCell (str): Represents a dead cell.
        DeadRedCell (str): Represents a dead red cell (typically poisonous).
        PinkCell (str): Represents a pink cell (typically a super predator).
        OrangeCell (str): Represents an orange cell (typically an herbivore).
    """
    EmptyCell = 'EmptyCell'
    EnergyCell = 'EnergyCell'
    GreenCell = 'GreenCell'
    RedCell = 'RedCell'
    PurpleCell = 'PurpleCell'
    YellowCell = 'YellowCell'
    DeadCell = 'DeadCell'
    DeadRedCell = 'DeadRedCell'
    PinkCell = 'PinkCell'
    OrangeCell = 'OrangeCell'

    def __new__(cls, value):
        """
        Initialize a new instance of the CellType Enum.

        This method is called when a new instance of the Enum is created.
        It populates a dictionary `cell_type__map` with the corresponding classes
        from the `cells` module based on the Enum values.

        Parameters:
        cls (CellType): The class of the Enum.
        value (str): The value of the Enum instance.

        Returns:
        CellType: A new instance of the CellType Enum.
        """
        obj = object.__new__(cls)

        cells = importlib.import_module(".cell_types", "cells")
        obj.cell_type__map = {
            cell: cells.__dict__.get(cell, None)
            for cell in cells.__dict__.get('__all__', [])
        }
        return obj

    @property
    def class_(self) -> Type[TCell]:
        """
        The class of the Enum member.

        Returns:
        class: The class corresponding to the Enum value.
        """
        return self.cell_type__map[self.value]

    @classmethod
    def get_poison_cells(cls) -> CellArray:
        """
        Get the names of poison cells.

        Returns:
        CellArray: A tuple containing the names of poison cells.
        """
        return (
            cls.DeadRedCell.value,
        )

    @classmethod
    def get_mutable_cells(cls) -> CellArray:
        """
        Get the names of mutable cells.

        Returns:
        CellArray: A tuple containing the names of mutable cells.
        """
        return (
            cls.RedCell.value,
            cls.PurpleCell.value,
            cls.GreenCell.value,
            cls.YellowCell.value,
        )

    @classmethod
    def get_immutable_cells(cls) -> CellArray:
        """
        Get the names of immutable cells.

        Returns:
        CellArray: A tuple containing the names of immutable cells.
        """
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_predators(cls) -> CellArray:
        """
        Get the names of predator cells.

        Returns:
        CellArray: A tuple containing the names of predator cells.
        """
        return (
            cls.PurpleCell.value,
            cls.RedCell.value,
        )

    @classmethod
    def get_super_predators(cls) -> CellArray:
        """
        Get the names of super predator cells.

        Returns:
        CellArray: A tuple containing the names of super predator cells.
        """
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_herbivores(cls) -> CellArray:
        """
        Get the names of herbivore cells.

        Returns:
        CellArray: A tuple containing the names of herbivore cells.
        """
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.OrangeCell.value,
        )

    @classmethod
    def get_energy_consumers(cls) -> CellArray:
        """
        Get the names of energy consumer cells.

        Returns:
        CellArray: A tuple containing the names of energy consumer cells.
        """
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.PurpleCell.value,
            cls.RedCell.value,
            cls.PinkCell.value,
            cls.OrangeCell.value,
        )
