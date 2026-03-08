from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from uuid import UUID


class UUIDGenerator(Protocol):
    def __call__(self) -> UUID:
        pass
