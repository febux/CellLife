from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class BaseGenome:
    neighbors_amounts_to_kill: Optional[Tuple[int, ...]] = None
    neighbors_to_reproduction: Optional[int] = None

    energy_boost__rate: Optional[float] = None
    cell_boost__rate: Optional[float] = None
    energy_consumption__rate: Optional[float] = None
    poison_rate: Optional[float] = None

    def to_bytes(self):
        pass
