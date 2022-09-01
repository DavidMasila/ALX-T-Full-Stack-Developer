"""empty message

Revision ID: 46117a3db2a7
Revises: 3ca0b9d73653
Create Date: 2022-08-31 04:31:38.972216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46117a3db2a7'
down_revision = '3ca0b9d73653'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.VARCHAR(),
               nullable=True)


    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL')

    op.alter_column('todos','completed',nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###s
    op.alter_column('todos', 'completed',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
