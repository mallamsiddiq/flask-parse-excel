"""relationship table to reflect years active

Revision ID: 760de2bfe559
Revises: 29fa40098649
Create Date: 2023-04-09 15:01:46.792830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '760de2bfe559'
down_revision = '29fa40098649'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('years_active', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['Units.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('employments')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employments',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('unit_id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=50), nullable=True),
    sa.Column('years_active', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['Units.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], )
    )
    op.drop_table('employment')
    # ### end Alembic commands ###