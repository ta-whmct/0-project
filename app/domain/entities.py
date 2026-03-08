from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from uuid import UUID

    from app.domain.constants import BunkerGateState
    from app.domain.value_objects import ProductMetric


@dataclass(slots=True)
class BunkerGate:
    state: BunkerGateState


@dataclass(slots=True)
class Bunker:
    uuid: UUID
    product_type: str
    max_volume: ProductMetric
    current_volume: ProductMetric
    pre_close_value: ProductMetric
