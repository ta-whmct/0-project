from typing import Annotated
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status

from app.application.dto.bunker import NewBunker
from app.application.interactors.bunker.create_bunker import CreateBunkerInteractor
from app.application.interactors.bunker.depends import new_bunker_dep
from app.application.interactors.bunker.get_bunker import GetBunkerInteractor
from app.application.interactors.bunker.get_bunker_list import GetBunkerListInteractor
from app.application.interactors.bunker.update_max_volume import (
    SetBunkerMaxVolumeInteractor,
)
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
async def get_bunker_list_endpoint(
    get_bunker_list: FromDishka[GetBunkerListInteractor],
) -> list[entities.Bunker]:
    bunkers = await get_bunker_list()
    return bunkers


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BunkerReadSchema)
async def create_bunker_endpoint(
    new_bunker: Annotated[NewBunker, Depends(new_bunker_dep)],
    create_bunker: FromDishka[CreateBunkerInteractor],
) -> entities.Bunker:
    return await create_bunker(new_bunker)


@router.get(
    "/{bunker_id}/",
    response_model=BunkerReadSchema,
)
async def get_bunker_by_id_endpoint(
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


@router.patch(
    "/{bunker_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_bunker_by_id_endpoint(
    bunker_id: Annotated[
        UUID,
        Path(description="Bunker ID", title="Bunker ID"),
    ],
    volume: Annotated[
        int, Query(description="Bunker max volume", title="Bunker max volume")
    ],
    set_max_volume: FromDishka[SetBunkerMaxVolumeInteractor],
) -> None:
    await set_max_volume(bunker_id, volume)
