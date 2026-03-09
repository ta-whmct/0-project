from dataclasses import dataclass


@dataclass
class NewBunker:
    product_type: str
    max_volume: int
    current_volume: int
    pre_close_value: int
    name: str


@dataclass
class UpdateBunker:
    max_volume: int | None
    current_volume: int | None
    pre_close_value: int | None
