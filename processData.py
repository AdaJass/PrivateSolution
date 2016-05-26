#-*- coding: utf-8 -*-

import asyncio
from pyquery import PyQuery as pq
import config
import json
from datetime import datetime as dt, timedelta as td
from aiomysql.sa import create_engine
from datetime import datetime
import random as rand

from model import *


@asyncio.coroutine
def Database(future):
    '''
    data is from the http response in main module.
    '''
    global engine
    engine = yield from create_engine(user='root',db='Currency',port=3306,
                                     host='127.0.0.1', password='11111')
    # yield from create_table(engine)

    # with (yield from engine) as conn:
    #     yield from conn.execute(tbl.insert().values(val='sag34'))
    #     yield from conn.execute('commit')        
    #     res = yield from conn.execute(tbl.select(tbl.c.id))
    #     print('ok')
    #     for row in res:
    #         print(row.id)

    future.set_result(engine)


@asyncio.coroutine
def CloseDB():
    engine.close()
    yield from engine.wait_closed()    
    pass

@asyncio.coroutine
def Xm(data):
    d = pq(data)
    d = d('div#dashboard-wrap')    
    ratioList={}
    for i in range(11):
        seltct=d('i.red-bar-nbr').eq(i).text()
        if seltct:
            ratioList[d('b').eq(i).text()] = float(seltct)
        pass 
        print(seltct) 

    #print(ratioList)  
    ratioList['XAUUSD']=ratioList['GOLD']
    ratioList['XAGUSD']=ratioList['SILVER']
    ratioList['DATE']=datetime.now()
    del ratioList['GOLD'] 
    del ratioList['SILVER']

    with (yield from engine) as conn:
        yield from conn.execute(xm.insert(),ratioList)
        yield from conn.execute('commit')

        res = yield from conn.execute(xm.select())
        for row in res:
            print(row)    
    pass

@asyncio.coroutine
def Atos(data):
    data=json.loads(data[13:-1])
    data=data['data']['ratioList']
    ratioList={}
    for x in data:
        k=x['value'].split(':')
        ratioList[x['symbol']] = float(k[1][0:-1])
    #print(ratioList)
    ratioList['OIL']=ratioList['USOIL']
    ratioList['DATE']=datetime.now()
    del ratioList['USOIL']
    del ratioList['UKOIL']
    with (yield from engine) as conn:
        yield from conn.execute(atos.insert(),ratioList)
        yield from conn.execute('commit')

        res = yield from conn.execute(atos.select())
        for row in res:
            print(row)
    pass 

@asyncio.coroutine
def Calendar(data):
    d=pq(data)
    s=d('tr[id^=eventRowId]')
    f=open('Calendar.txt','w',encoding='utf-8')
    for i in s.items():
        tem=i('td.sentiment').attr('title')
        if tem and tem[-1]=='高':
            time=i.attr('event_timestamp')
            t1=dt.strptime(time,'%Y-%m-%d %H:%M:%S')
            t1=t1+td(hours=8)
            time=dt.strftime(t1,'%Y-%m-%d %H:%M:%S')
            t2=dt.now()
            delta=t1-t2
            if 0<=delta.days<2:                
                f.write(time+'    ')
                country=i('td.flagCur span').attr('title')                
                f.write(country+'   ')
                f.write(i('td.event').text()+'\n\n')
    f.close()
    
    pass


if __name__ == '__main__':
    Xm('<a>hello</a>')     