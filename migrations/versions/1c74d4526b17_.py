"""empty message

Revision ID: 1c74d4526b17
Revises: 63922dd222f9
Create Date: 2020-03-01 19:06:12.654771

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1c74d4526b17'
down_revision = '63922dd222f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'userRole')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('userRole', mysql.ENUM('ADMIN', 'USER'), nullable=False))
    # ### end Alembic commands ###
