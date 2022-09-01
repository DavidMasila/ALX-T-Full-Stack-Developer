"""empty message

Revision ID: 24dd19e76835
Revises: 1226402c0a8f
Create Date: 2022-08-30 05:10:56.832484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24dd19e76835'
down_revision = '1226402c0a8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('completed', sa.String(), nullable=True),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['todolist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('stuff')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stuff',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('completed', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('list_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['todolist.id'], name='stuff_list_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='stuff_pkey')
    )
    op.drop_table('todos')
    # ### end Alembic commands ###
