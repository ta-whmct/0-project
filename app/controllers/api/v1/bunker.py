from typing import Annotated
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, HTTPException, Path
from starlette import status

from app.application.interactors.bunker.get_bunker import GetBunkerInteractor
from app.application.interactors.bunker.get_bunker_list import GetBunkerListInteractor
from app.config.constants import ApiV1Endpoints
from app.controllers.schemas.bunker import BunkerReadSchema
from app.domain import entities

router = APIRouter(
    prefix=ApiV1Endpoints.bunker.value["name"],
    tags=ApiV1Endpoints.bunker.value["tags"],
    route_class=DishkaRoute,
)


@router.get(
    "",
    response_model=list[BunkerReadSchema],
)
async def get_bunker_list(
    get_bunker_list: FromDishka[GetBunkerListInteractor],
) -> list[entities.Bunker] | None:
    bunkers = await get_bunker_list()
    if bunkers is not None:
        return bunkers
    return None


@router.get(
    "/{bunker_id}/",
    response_model=BunkerReadSchema,
)
async def get_bunker_by_id(
    bunker_id: Annotated[
        UUID,
        Path(description="Bunker ID", title="Bunker ID"),
    ],
    get_bunker: FromDishka[GetBunkerInteractor],
) -> entities.Bunker:
    bunker = await get_bunker(bunker_id)
    if bunker is not None:
        return bunker

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Bunker {bunker_id} not found.",
    )
