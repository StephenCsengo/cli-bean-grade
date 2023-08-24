"""Add Rating model

Revision ID: fa96baa619bd
Revises: d812c30d349b
Create Date: 2023-08-23 11:33:17.418191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa96baa619bd'
down_revision: Union[str, None] = 'd812c30d349b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
