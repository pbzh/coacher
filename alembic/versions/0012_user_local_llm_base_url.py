"""Add per-user local LLM base URL override

Revision ID: 0012_user_local_llm_base_url
Revises: 0011_normalize_null_api_keys
Create Date: 2026-05-04

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0012_user_local_llm_base_url"
down_revision: str | None = "0011_normalize_null_api_keys"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "userprofile",
        sa.Column("local_llm_base_url", sa.String(length=1024), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("userprofile", "local_llm_base_url")
