"""empty message

Revision ID: 907951c7a357
Revises: 
Create Date: 2020-04-29 01:45:02.689337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907951c7a357'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rss_url',
    sa.Column('url', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('url'),
    sa.UniqueConstraint('url')
    )
    op.create_table('user',
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('rss_url')
    # ### end Alembic commands ###