"""empty message

Revision ID: 41e53f5f3b1b
Revises: 7d7017b32796
Create Date: 2017-06-15 06:48:43.511798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '41e53f5f3b1b'
down_revision = '7d7017b32796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('author', 'password',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=60),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'password',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
