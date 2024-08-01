from typing import List, TypeAlias, Tuple

from cells.cell_types.abstract_cell import TCell

Vector: TypeAlias = List[TCell]
Matrix: TypeAlias = List[Vector]
CellArray: TypeAlias = Tuple[str, ...]
