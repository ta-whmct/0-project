from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.database import DatabaseConfig


def new_engine(
    db_config: DatabaseConfig,
) -> AsyncEngine:
    return create_async_engine(
        url=db_config.async_url,
        pool_size=db_config.sqla.pool_size,
        max_overflow=db_config.sqla.max_overflow,
        connect_args=db_config.sqla.connect_args,
    )


def new_session_maker(
    async_engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        expire_on_commit=False,
    )
