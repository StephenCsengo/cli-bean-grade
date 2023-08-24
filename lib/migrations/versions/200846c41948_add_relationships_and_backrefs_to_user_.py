"""Add relationships and backrefs to User and Coffee models

Revision ID: 200846c41948
Revises: fa96baa619bd
Create Date: 2023-08-23 11:35:57.918906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '200846c41948'
down_revision: Union[str, None] = 'fa96baa619bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
