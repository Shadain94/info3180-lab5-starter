"""empty message

Revision ID: 17e04d5ed2a4
Revises: f2fc4bbe096a
Create Date: 2017-02-23 17:02:34.728451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e04d5ed2a4'
down_revision = 'f2fc4bbe096a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
