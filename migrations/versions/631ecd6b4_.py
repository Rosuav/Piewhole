"""empty message

Revision ID: 631ecd6b4
Revises: 5129f84ce10
Create Date: 2015-07-30 12:29:48.975166

"""

# revision identifiers, used by Alembic.
revision = '631ecd6b4'
down_revision = '5129f84ce10'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Ranks', sa.Column('rankdesc', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'Ranks', ['rankdesc'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Ranks', type_='unique')
    op.drop_column('Ranks', 'rankdesc')
    ### end Alembic commands ###
