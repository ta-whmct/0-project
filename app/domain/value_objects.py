from dataclasses import dataclass


@dataclass
class ProductMetric:
    value: float
    unit_measure: str = "t"
