from enum import Enum
from typing import Tuple
import importlib


class CellType(Enum):
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
            'EmptyCell': cells.EmptyCell,
            'EnergyCell': cells.EnergyCell,
            'GreenCell': cells.GreenCell,
            'RedCell': cells.RedCell,
            'PurpleCell': cells.PurpleCell,
            'YellowCell': cells.YellowCell,
            'DeadCell': cells.DeadCell,
            'DeadRedCell': cells.DeadRedCell,
            'PinkCell': cells.PinkCell,
            'OrangeCell': cells.OrangeCell,
        }
        return obj

    @property
    def class_(self):
        """
        The class of the Enum member.

        Returns:
        class: The class corresponding to the Enum value.
        """
        # return self._class_
        return self.cell_type__map[self.value]

    @classmethod
    def get_poison_cells(cls) -> Tuple[str, ...]:
        """
        Get the names of poison cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of poison cells.
        """
        return (
            cls.DeadRedCell.value,
        )

    @classmethod
    def get_mutable_cells(cls) -> Tuple[str, ...]:
        """
        Get the names of mutable cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of mutable cells.
        """
        return (
            cls.RedCell.value,
            cls.PurpleCell.value,
            cls.GreenCell.value,
            cls.YellowCell.value,
        )

    @classmethod
    def get_immutable_cells(cls) -> Tuple[str, ...]:
        """
        Get the names of immutable cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of immutable cells.
        """
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_predators(cls) -> Tuple[str, ...]:
        """
        Get the names of predator cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of predator cells.
        """
        return (
            cls.PurpleCell.value,
            cls.RedCell.value,
        )

    @classmethod
    def get_super_predators(cls) -> Tuple[str, ...]:
        """
        Get the names of super predator cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of super predator cells.
        """
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_herbivores(cls) -> Tuple[str, ...]:
        """
        Get the names of herbivore cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of herbivore cells.
        """
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.OrangeCell.value,
        )

    @classmethod
    def get_energy_consumers(cls) -> Tuple[str, ...]:
        """
        Get the names of energy consumer cells.

        Returns:
        Tuple[str, ...]: A tuple containing the names of energy consumer cells.
        """
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.PurpleCell.value,
            cls.RedCell.value,
            cls.PinkCell.value,
            cls.OrangeCell.value,
        )
