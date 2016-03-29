import sqlalchemy as sa


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))

xm= sa.Table('xm', metadata,
            sa.Column('id',sa.Integer, primary_key=True),
            sa.Column('EUR',sa.Float(8)),
            sa.Column('GBP',sa.Float(8)),
            sa.Column('XAU',sa.Float(8)),
            sa.Column('JPY',sa.Float(8)),
            sa.Column('OIL',sa.Float(8)),
            sa.Column('JP225',sa.Float(8)),
            sa.Column('SIL',sa.Float(8)),
            sa.Column('UU',sa.Float(8)),
            sa.Column('EUR',sa.Float(8)),
            sa.Column('GBP',sa.Float(8))
    )

def create_table(engine):
    with (yield from engine) as conn:
        yield from conn.execute('DROP TABLE IF EXISTS tbl')
        yield from conn.execute('''CREATE TABLE tbl (
                                            id serial PRIMARY KEY,
                                            val varchar(255))''')