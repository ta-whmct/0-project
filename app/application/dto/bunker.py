from dataclasses import dataclass


@dataclass
class NewBunker:
    product_type: str
    max_volume: int
    current_volume: int
    pre_close_value: int
    name: str
