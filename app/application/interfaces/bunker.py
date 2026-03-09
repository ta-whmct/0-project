from typing import Protocol
from uuid import UUID

from app.domain.entities import Bunker


class BunkerSaver(Protocol):
    async def save(self, bunker: Bunker) -> None: ...


class BunkerReader(Protocol):
    async def read_by_uuid(self, uuid: UUID) -> Bunker | None: ...

    async def read(self) -> list[Bunker]: ...


class UsersReader(Protocol):
    async def read(self) -> list[Bunker]: ...
