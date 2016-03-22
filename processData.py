import asyncio
import pyquery as pq
import config

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
    d=pq.PyQuery(data)

    print(d('p:first'))
    pass

async def Asto(data):
    d=pq.PyQuery(data)
    print(d(''))
    pass 

async def Calendar(data):
    d=pq.PyQuery(data)
    print(data[1000:1050])
    pass

if __name__ == '__main__':
    processData('<a>hello</a>')            