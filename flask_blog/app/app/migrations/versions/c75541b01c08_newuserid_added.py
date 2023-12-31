"""newuserid_added

Revision ID: c75541b01c08
Revises: 842b14a253da
Create Date: 2023-11-18 11:51:02.000727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c75541b01c08'
down_revision = '842b14a253da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.String(length=128), nullable=True))
        batch_op.create_unique_constraint('userid', ['userid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('userid', type_='unique')
        batch_op.drop_column('userid')

    # ### end Alembic commands ###
