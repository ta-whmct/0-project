from uuid import UUID

from app.application.interfaces.bunker import BunkerReader
from app.domain.entities import Bunker


class GetBunkerInteractor:
    def __init__(self, reader: BunkerReader) -> None:
        self._reader = reader

    async def __call__(self, uuid: UUID) -> Bunker | None:
        return await self._reader.read_by_uuid(uuid=uuid)
