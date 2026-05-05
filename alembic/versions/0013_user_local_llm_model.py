"""Add per-user local LLM model override

Revision ID: 0013_user_local_llm_model
Revises: 0012_user_local_llm_base_url
Create Date: 2026-05-04

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0013_user_local_llm_model"
down_revision: str | None = "0012_user_local_llm_base_url"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("userprofile", sa.Column("local_llm_model", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("userprofile", "local_llm_model")
