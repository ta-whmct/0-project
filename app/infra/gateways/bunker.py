from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.bunker import BunkerReader, BunkerSaver
from app.domain.entities import Bunker
from app.infra import models


class BunkerGateway(BunkerReader, BunkerSaver):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def read_by_uuid(self, uuid: UUID) -> Bunker | None:
        bunker = (
            await self._session.execute(select(models.Bunker).filter_by(id=uuid))
        ).scalar_one_or_none()
        if bunker is None:
            return None
        return Bunker(
            id=bunker.id,
            max_volume=bunker.max_volume,
            current_volume=bunker.current_volume,
            pre_close_value=bunker.pre_close_value,
            product_type=bunker.product_type,
        )

    async def save(self, bunker: Bunker) -> None:
        bunker_model = models.Bunker(
            id=bunker.id,
            max_volume=bunker.max_volume,
            current_volume=bunker.current_volume,
            pre_close_value=bunker.pre_close_value,
            product_type=bunker.product_type,
        )
        self._session.add(bunker_model)

    async def read(self) -> list[Bunker]:
        stmt = select(models.Bunker).order_by(models.Bunker.id)
        bunkers = await self._session.scalars(stmt)
        return [
            Bunker(
                id=bunker.id,
                product_type=bunker.product_type,
                max_volume=bunker.max_volume,
                current_volume=bunker.current_volume,
                pre_close_value=bunker.pre_close_value,
            )
            for bunker in bunkers.all()
        ]
