"""empty message

Revision ID: 22b7d3f5dd5d
Revises: f0c876cf65b2
Create Date: 2022-03-01 20:28:35.989033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22b7d3f5dd5d'
down_revision = 'f0c876cf65b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('starship', sa.String(length=250), nullable=True),
    sa.Column('vehicles', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=True),
    sa.Column('rotation_period', sa.String(length=250), nullable=True),
    sa.Column('orbital_period', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('residents', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('vehicle_class', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('lenth', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=250), nullable=True),
    sa.Column('crew', sa.String(length=250), nullable=True),
    sa.Column('passengers', sa.String(length=250), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=250), nullable=True),
    sa.Column('consumable', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('character_fav', sa.Integer(), nullable=True),
    sa.Column('planet_fav', sa.Integer(), nullable=True),
    sa.Column('vehicle_fav', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_fav'], ['character.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['planet_fav'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['vehicle_fav'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
