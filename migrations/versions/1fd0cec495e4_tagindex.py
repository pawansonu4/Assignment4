"""tagindex

Revision ID: 1fd0cec495e4
Revises: 50897c4019fd
Create Date: 2014-10-05 15:50:27.041467

"""

# revision identifiers, used by Alembic.
revision = '1fd0cec495e4'
down_revision = '50897c4019fd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_tag_name'), 'tag', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_name'), table_name='tag')
    ### end Alembic commands ###