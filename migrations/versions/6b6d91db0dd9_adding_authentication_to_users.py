"""adding authentication to users

Revision ID: 6b6d91db0dd9
Revises: f001f6d7ccbc
Create Date: 2023-04-10 14:53:08.992545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6d91db0dd9'
down_revision = 'f001f6d7ccbc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('password', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'password')
    # ### end Alembic commands ###
