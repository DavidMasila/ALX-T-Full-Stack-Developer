"""empty message

Revision ID: 573a11bf261f
Revises: 07399d2dd2e2
Create Date: 2022-08-31 03:55:45.928738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573a11bf261f'
down_revision = '07399d2dd2e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
