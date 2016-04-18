#-*- coding: utf-8 -*-

import asyncio
import config
import json
from datetime import datetime as dt, timedelta as td
from processData import Database
from model import *




@asyncio.coroutine
def Draw(engine):    
    with (yield from engine) as conn:        
        res = yield from conn.execute(xm.select())
        for row in res:
            print(row.DATE, row.EURUSD)
      
    pass