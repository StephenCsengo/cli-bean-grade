"""Remove date received from coffees table

Revision ID: d8065b60ae56
Revises: 7c98ebbec651
Create Date: 2023-08-24 14:33:47.596562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8065b60ae56'
down_revision: Union[str, None] = '7c98ebbec651'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###