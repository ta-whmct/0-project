from app.application.dto.bunker import NewBunker
from app.controllers.schemas.bunker import BunkerCreateSchema


def new_bunker_dep(
    bunker_create: BunkerCreateSchema,
) -> NewBunker:
    return NewBunker(
        product_type=bunker_create.product_type,
        max_volume=bunker_create.max_volume,
        current_volume=bunker_create.current_volume,
        pre_close_value=bunker_create.pre_close_value,
        name=bunker_create.name,
    )
