import asyncio
from pyquery import PyQuery as pq
import config

import json
if config.MYSQL:
    import aiomysql

@asyncio.coroutine
def processData(data):
    '''
    data is from the http response in main module.
    '''
    
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

async def Asto(data):
    data=json.loads(data[13:-1])
    data=data['data']['ratioList']
    ratioList={}
    for x in data:
        k=x['value'].split(':')
        ratioList[x['symbol']] = float(k[0][0:-1])

    print(ratioList)

    pass 

async def Calendar(data):
    d=pq(data)
    print(data)
    pass

if __name__ == '__main__':
    processData('<a>hello</a>') 