"""empty message

Revision ID: 3f152409196f
Revises: 4accbf4bf3b9
Create Date: 2016-12-04 20:59:53.603438

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3f152409196f'
down_revision = '4accbf4bf3b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=Text()), autoincrement=False, nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='results_pkey')
    )
    # ### end Alembic commands ###
