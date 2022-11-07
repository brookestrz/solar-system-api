"""Added moon model and blueprint

Revision ID: b0ac3b3d0238
Revises: 2391ae7d2862
Create Date: 2022-11-04 11:07:22.222570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ac3b3d0238'
down_revision = '2391ae7d2862'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('planet', sa.Column('moon_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'planet', 'moon', ['moon_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'planet', type_='foreignkey')
    op.drop_column('planet', 'moon_id')
    op.drop_table('moon')
    # ### end Alembic commands ###
