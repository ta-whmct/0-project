from uuid import UUID

from app.application.dto.bunker import NewBunker
from app.application.interfaces.bunker import BunkerSaver
from app.application.interfaces.uuid_generator import UUIDGenerator
from app.domain.entities import Bunker


class CreateBunkerInteractor:
    def __init__(self, saver: BunkerSaver, uuid_generator: UUIDGenerator) -> None:
        self._saver = saver
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: NewBunker) -> UUID:
        uuid = self._uuid_generator()
        bunker = Bunker(
            id=uuid,
            max_volume=dto.max_volume,
            pre_close_value=dto.pre_close_value,
            current_volume=dto.current_volume,
            product_type=dto.product_type,
        )
        await self._saver.save(bunker)
        return uuid
