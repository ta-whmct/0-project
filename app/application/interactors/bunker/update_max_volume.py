from uuid import UUID

from app.application.interactors.transaction_manager import TransactionManagerAsync
from app.application.interfaces.bunker import BunkerSetter


class SetBunkerMaxVolumeInteractor:
    def __init__(
        self, trx_manager: TransactionManagerAsync, setter: BunkerSetter
    ) -> None:
        self._trx_manager = trx_manager
        self._setter = setter

    async def __call__(self, uuid: UUID, volume: int) -> None:

        await self._setter.set_max_volume(uuid, volume)
        await self._trx_manager.commit()
