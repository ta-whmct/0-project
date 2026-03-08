from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from uuid import UUID

    from app.domain.constants import BunkerGateState


@dataclass(slots=True)
class BunkerGate:
    state: BunkerGateState


@dataclass(slots=True)
class Bunker:
    id: UUID
    product_type: str
    max_volume: int
    current_volume: int
    pre_close_value: int
