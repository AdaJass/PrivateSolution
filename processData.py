#-*- coding: utf-8 -*-

import asyncio
from pyquery import PyQuery as pq
import config
import json
from datetime import datetime as dt, timedelta as td
from aiomysql.sa import create_engine

from model import *


@asyncio.coroutine
def Database(loop):
    '''
    data is from the http response in main module.
    '''
    global engine
    engine = yield from create_engine(user='jass',db='test',port=3306,\
                                        host='127.0.0.1', password='11111')


    yield from create_table(engine)

    with (yield from engine) as conn:
        yield from conn.execute(tbl.insert(),{"val":'abc',"id":1})

        res = yield from conn.execute(tbl.select())
        for row in res:
            print(row.id, row.val)


    pass


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
        ratioList[d('b').eq(i).text()] = float(d('span').eq(i*2).attr('data-percentage'))
        pass     
        
    print(ratioList)
    pass

@asyncio.coroutine
def Asto(data):
    data=json.loads(data[13:-1])
    data=data['data']['ratioList']
    ratioList={}
    for x in data:
        k=x['value'].split(':')
        ratioList[x['symbol']] = float(k[0][0:-1])

    print(ratioList)

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
            t1=t1+td(hours=6)
            time=dt.strftime(t1,'%Y-%m-%d %H:%M:%S')
            t2=dt.now()
            delta=t1-t2
            if 0<=delta.days<2:                
                f.write(time+'    ')
                f.write(i('td.event').html()+'\n\n')
    f.close()
    pass

if __name__ == '__main__':
    Xm('<a>hello</a>')    