from typing import List, TypeAlias, Tuple, TypeVar


TCell = TypeVar("TCell", bound="Cell")

Vector: TypeAlias = List[TCell]
Matrix: TypeAlias = List[Vector]
CellArray: TypeAlias = Tuple[str, ...]
