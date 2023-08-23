"""Add User and Coffee models

Revision ID: d812c30d349b
Revises: 8e10646d238a
Create Date: 2023-08-23 11:25:03.234639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd812c30d349b'
down_revision: Union[str, None] = '8e10646d238a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
