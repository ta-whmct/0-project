import uuid
from collections.abc import AsyncGenerator

from dishka import AnyOf, Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from app.application.interactors.bunker.create_bunker import CreateBunkerInteractor
from app.application.interactors.bunker.get_bunker import GetBunkerInteractor
from app.application.interactors.transaction_manager import TransactionManagerAsync
from app.application.interfaces.bunker import BunkerReader, BunkerSaver
from app.application.interfaces.uuid_generator import UUIDGenerator
from app.config.settings import settings
from app.infra.database import new_engine, new_session_maker
from app.infra.gateways.bunker import BunkerGateway


class AppProvider(Provider):
    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        return uuid.uuid7

    @provide(scope=Scope.APP)
    async def get_engine(self) -> AsyncGenerator[AsyncEngine]:
        engine = new_engine(settings.db)
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    def get_session_maker(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self,
        session_maker: async_sessionmaker[AsyncSession],
    ) -> AsyncGenerator[AnyOf[AsyncSession, TransactionManagerAsync]]:
        async with session_maker() as session:
            yield session

    bunker_gateway = provide(
        BunkerGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            BunkerReader,
            BunkerSaver,
        ],
    )

    get_bunker_interactor = provide(
        GetBunkerInteractor,
        scope=Scope.REQUEST,
    )

    create_new_bunker_interactor = provide(
        CreateBunkerInteractor,
        scope=Scope.REQUEST,
    )
