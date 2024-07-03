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
        """The class of the Enum member."""
        # return self._class_
        return self.cell_type__map[self.value]

    @classmethod
    def get_poison_cells(cls) -> Tuple[str, ...]:
        return (
            cls.DeadRedCell.value,
        )

    @classmethod
    def get_mutable_cells(cls) -> Tuple[str, ...]:
        return (
            cls.RedCell.value,
            cls.PurpleCell.value,
            cls.GreenCell.value,
            cls.YellowCell.value,
        )

    @classmethod
    def get_immutable_cells(cls) -> Tuple[str, ...]:
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_predators(cls) -> Tuple[str, ...]:
        return (
            cls.PurpleCell.value,
            cls.RedCell.value,
        )

    @classmethod
    def get_super_predators(cls) -> Tuple[str, ...]:
        return (
            cls.PinkCell.value,
        )

    @classmethod
    def get_herbivores(cls) -> Tuple[str, ...]:
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.OrangeCell.value,
        )

    @classmethod
    def get_energy_consumers(cls) -> Tuple[str, ...]:
        return (
            cls.GreenCell.value,
            cls.YellowCell.value,
            cls.PurpleCell.value,
            cls.RedCell.value,
            cls.PinkCell.value,
            cls.OrangeCell.value,
        )
