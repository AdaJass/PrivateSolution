import asyncio

@asyncio.coroutine
def slow_operation(future):
    future.set_result('Future is done!')
    yield from asyncio.sleep(5)
    future.set_result('Future are done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print(future.result())
loop.close()
