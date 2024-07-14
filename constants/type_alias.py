from typing import List, TypeAlias, Tuple

from cells.abstract_cell import TCell

Vector: TypeAlias = List[TCell]
Matrix: TypeAlias = List[Vector]
CellArray: TypeAlias = Tuple[str, ...]
