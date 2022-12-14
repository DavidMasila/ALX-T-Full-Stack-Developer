"""empty message

Revision ID: 53bb228ec5f5
Revises: 7bbb6e03b1b5
Create Date: 2022-09-17 23:34:02.553571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bb228ec5f5'
down_revision = '7bbb6e03b1b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('scientific_name', sa.String(), nullable=True),
    sa.Column('is_poisonous', sa.Boolean(), nullable=True),
    sa.Column('primary_color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('plant')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('scientific_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_poisonous', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('primary_color', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='plant_pkey')
    )
    op.drop_table('plants')
    # ### end Alembic commands ###
