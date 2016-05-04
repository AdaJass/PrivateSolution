#-*- coding: utf-8 -*-

import asyncio
import matplotlib.pyplot as plt
from model import *
import os
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
        res = yield from conn.execute(xm.select().order_by(xm.c.DATE))
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
        res = yield from conn.execute(atos.select().order_by(atos.c.DATE))
        for row in res:
            DATE.append(row.DATE)            
            for name in ATOS.keys():
                ATOS[name].append(row[name])

        for name in ATOS.keys():
            fig=plt.figure()
            plt.plot(DATE, ATOS[name])
            fig.autofmt_xdate()
            plt.savefig('./imagines/ATOS_'+ name+'.jpg')
            plt.close()
    os.system('copy imagines\\*.*  ..\\HotIO\\public\\private_images')      
    pass

if __name__ == '__main__':
	os.system('copy imagines\\*.*  ..\\HotIO\\public\\private_images')
	