#-*- coding: utf-8 -*-

import asyncio
import matplotlib.pyplot as plt
from datetime import datetime as dt, timedelta as td
from model import *
import os

thrashold=dt.now()-td(days=4)

@asyncio.coroutine
def delData(engine):    
    with (yield from engine) as conn:
        yield from conn.execute(xm.delete().where(xm.c.DATE<thrashold))
        yield from conn.execute(atos.delete().where(atos.c.DATE<thrashold))
        yield from conn.execute('commit')
    pass


@asyncio.coroutine
def Draw(engine):
    XM={
        'EURUSD':[],
        'USDJPY':[],
        'GBPUSD':[],
        'XAUUSD':[],
        'XAGUSD':[],
        'OIL':[],
        'US30':[],
        'JP225':[],
        'EURJPY':[],
        'GBPJPY':[],
        'GER30':[]
    }
    ATOS={
        'EURUSD':[],
        'USDJPY':[],
        'GBPUSD':[],
        'XAUUSD':[],
        'XAGUSD':[],
        'OIL':[],
        'US30':[],
        'AUDUSD':[],
        'HKG50':[]    
    }
    DATE=[]
    with (yield from engine) as conn:        
        res = yield from conn.execute(xm.select().where(xm.c.DATE>thrashold).order_by(xm.c.DATE))
        for row in res:
            DATE.append(row.DATE)
            for name in XM.keys():
                XM[name].append(row[name])

        for name in XM.keys():
            fig=plt.figure()
            plt.plot(DATE, XM[name])
            fig.autofmt_xdate()
            plt.savefig('./imagines/XM_'+ name+'.jpg')
            plt.close()

        DATE=[]
        res = yield from conn.execute(atos.select().where(atos.c.DATE>thrashold).order_by(atos.c.DATE))
        for row in res:
            DATE.append(row.DATE)            
            for name in ATOS.keys():
                ATOS[name].append(row[name])

        # if(len(DATE)>430 or max(DATE)-min(DATE)> td(days=2.5)):
        #     yield from delData(engine) 

        for name in ATOS.keys():
            fig=plt.figure()
            plt.plot(DATE, ATOS[name])
            fig.autofmt_xdate()
            plt.savefig('./imagines/ATOS_'+ name+'.jpg')
            plt.close()
    os.system('copy imagines\\*.*  ..\\HotIO\\private\\private_images')
    os.system('copy Calendar.txt ..\\\\HotIO\\private\\')      
    pass

if __name__ == '__main__':
    os.system('copy Calendar.txt ..\\\\HotIO\\private\\')
    os.system('copy imagines\\*.*  ..\\HotIO\\private\\private_images')