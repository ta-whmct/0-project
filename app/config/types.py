from enum import Enum
from typing import TypedDict


class EndpointParams(TypedDict):
    name: str
    tags: list[str | Enum]


class BunkerNameConstrType(TypedDict):
    min: int
    max: int
