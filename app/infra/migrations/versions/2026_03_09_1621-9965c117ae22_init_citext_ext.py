"""init citext ext

Revision ID: 9965c117ae22
Revises: a91283d4e5be
Create Date: 2026-03-09 16:21:25.745084

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9965c117ae22"
down_revision: str | Sequence[str] | None = "a91283d4e5be"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS citext;")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP EXTENSION IF EXISTS citext;")
