import uuid

from sqlalchemy import UUID, CheckConstraint, Integer, String, and_, func
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import Mapped, mapped_column

from ...config.constants import BUNKER_NAME_CONSTR
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
    name: Mapped[str] = mapped_column(CITEXT, unique=True)

    __table_args__ = (
        CheckConstraint(
            and_(
                func.length(name) >= BUNKER_NAME_CONSTR["min"],
                func.length(name) <= BUNKER_NAME_CONSTR["max"],
            ),
            name="name_length",
        ),
    )
