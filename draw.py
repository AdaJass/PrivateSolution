#-*- coding: utf-8 -*-

import asyncio
import config
import json
from datetime import datetime as dt, timedelta as td
from processData import Database
from model import *
import matplotlib.pyplot as plt


EURUSD=[]
DATE=[]


@asyncio.coroutine
def Draw(engine):    
    with (yield from engine) as conn:        
        res = yield from conn.execute(xm.select())
        for row in res:
            DATE.append(row.DATE)
            EURUSD.append(row.EURUSD)

        fig=plt.figure()
        plt.plot(DATE, EURUSD)
        fig.autofmt_xdate()
        plt.show()
      
    pass