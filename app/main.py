from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.config.settings import settings
from app.controllers.api import router as api_router
from app.ioc.app import AppProvider

container = make_async_container(AppProvider())


@asynccontextmanager
async def lifespan(
    _: FastAPI,
) -> AsyncGenerator[None]:
    yield


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(
        title=settings.app.title,
        lifespan=lifespan,
    )

    fastapi_app.include_router(api_router)

    setup_dishka(container, fastapi_app)

    return fastapi_app


def get_app() -> FastAPI:
    return get_fastapi_app()


app = get_app()
