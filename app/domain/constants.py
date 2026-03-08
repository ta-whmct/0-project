from enum import StrEnum, unique


@unique
class BunkerGateState(StrEnum):
    opened = "opened"
    close = "closed"
