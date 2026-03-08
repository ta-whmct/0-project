from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.value_objects import ProductMetric


@dataclass
class NewBunker:
    product_type: str
    max_volume: ProductMetric
    current_volume: ProductMetric
    pre_close_value: ProductMetric
