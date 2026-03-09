from uuid import UUID

from pydantic import BaseModel


class BunkerBaseSchema(BaseModel):
    product_type: str
    max_volume: int
    current_volume: int
    pre_close_value: int


class BunkerCreateSchema(BunkerBaseSchema):
    pass


class BunkerReadSchema(BunkerBaseSchema):
    id: UUID
