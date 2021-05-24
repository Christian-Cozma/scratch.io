"""empty message

Revision ID: 41d020aeeb80
Revises: 
Create Date: 2021-05-24 12:00:13.053219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41d020aeeb80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('blurb', sa.String(length=255), nullable=True),
    sa.Column('avatarUrl', sa.String(length=255), nullable=True),
    sa.Column('githubUrl', sa.String(length=255), nullable=True),
    sa.Column('websiteUrl', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('blurb', sa.Text(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('github', sa.String(), nullable=True),
    sa.Column('recruiting', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('users_games',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('gameId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gameId'], ['games.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('userId', 'gameId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_games')
    op.drop_table('users')
    op.drop_table('teams')
    op.drop_table('skills')
    op.drop_table('games')
    # ### end Alembic commands ###
