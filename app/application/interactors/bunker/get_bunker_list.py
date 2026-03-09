from app.application.interfaces.bunker import BunkerReader
from app.domain.entities import Bunker


class GetBunkerListInteractor:
    def __init__(self, reader: BunkerReader) -> None:
        self._reader = reader

    async def __call__(self) -> list[Bunker] | None:
        return await self._reader.read()
