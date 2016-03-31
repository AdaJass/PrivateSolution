import sqlalchemy as sa
import asyncio

global xm, atos

metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))



xm = sa.Table('xm', metadata,
            sa.Column('DATE',sa.DateTime, primary_key=True),
            sa.Column('EURUSD',sa.Float(8)),
            sa.Column('GBPUSD',sa.Float(8)),
            sa.Column('USDJPY',sa.Float(8)),
            sa.Column('XAUUSD',sa.Float(8)),
            sa.Column('XAGUSD',sa.Float(8)),
            sa.Column('OIL',sa.Float(8)),
            sa.Column('US30',sa.Float(8)),
            sa.Column('GER30',sa.Float(8)),
            sa.Column('JP225',sa.Float(8)),            
            sa.Column('EURJPY',sa.Float(8)),            
            sa.Column('GBPJPY',sa.Float(8))
    )

atos = sa.Table('atos', metadata,
            sa.Column('DATE',sa.DateTime, primary_key=True),
            sa.Column('EURUSD',sa.Float(8)),
            sa.Column('GBPUSD',sa.Float(8)),
            sa.Column('USDJPY',sa.Float(8)),
            sa.Column('AUDUSD',sa.Float(8)), 
            sa.Column('XAUUSD',sa.Float(8)),
            sa.Column('XAGUSD',sa.Float(8)),            
            sa.Column('OIL',sa.Float(8)),                       
            sa.Column('HKG50',sa.Float(8)),
            sa.Column('US30',sa.Float(8))
    )


@asyncio.coroutine
def create_table(engine):
    with (yield from engine) as conn:
            yield from conn.execute('DROP TABLE IF EXISTS tbl')
            yield from conn.execute('''CREATE TABLE tbl (
                                                id serial PRIMARY KEY,
                                                val varchar(255))''')

