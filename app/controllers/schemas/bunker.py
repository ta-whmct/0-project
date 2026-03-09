from uuid import UUID

from pydantic import BaseModel, Field

from app.config.constants import BUNKER_NAME_CONSTR


class BunkerBaseSchema(BaseModel):
    product_type: str
    max_volume: int
    current_volume: int
    pre_close_value: int
    name: str = Field(
        min_length=BUNKER_NAME_CONSTR["min"], max_length=BUNKER_NAME_CONSTR["max"]
    )


class BunkerCreateSchema(BunkerBaseSchema):
    pass


class BunkerReadSchema(BunkerBaseSchema):
    id: UUID
