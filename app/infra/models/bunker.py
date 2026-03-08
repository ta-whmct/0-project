import uuid

from sqlalchemy import UUID, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Bunker(Base):
    __tablename__ = "bunker"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuidv7(),
    )
    product_type: Mapped[str] = mapped_column(
        String,
    )
    max_volume: Mapped[int] = mapped_column(Integer, comment="kg")
    current_volume: Mapped[int] = mapped_column(Integer, comment="kg")
    pre_close_value: Mapped[int] = mapped_column(Integer, comment=" kg")
