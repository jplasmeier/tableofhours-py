"""empty message

Revision ID: 71c2caf004ec
Revises: fc9b470bf9ed
Create Date: 2016-12-04 21:10:32.701214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71c2caf004ec'
down_revision = 'fc9b470bf9ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('is_completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_completed')
    # ### end Alembic commands ###