import asyncio
import random
import time


@asyncio.coroutine
def get_url(url):
    wait_time = random.randint(3 ,16)
    yield from asyncio.sleep(wait_time)
    print('URL {} took {}s to get!'.format(url, wait_time))
    return url, wait_time


@asyncio.coroutine
def process_as_results_come_in():
    before = time.time()
    coroutines = [get_url(url) for url in ['URL1', 'URL2', 'URL3']]
    for coroutine in asyncio.as_completed(coroutines):
        url, wait_time = yield from coroutine
        print('Coroutine for {} is done'.format(url))
    after = time.time()
    print('total time: {} seconds'.format(after - before))


@asyncio.coroutine
def process_once_everything_ready():
    before = time.time()
    coroutines = [get_url(url) for url in ['URL1', 'URL2', 'URL3']]
    results = yield from asyncio.gather(*coroutines)
    print(results)
    after = time.time()
    print('total time: {} seconds'.format(after - before))


def main():
    loop = asyncio.get_event_loop()
    print("First, process results as they come in:")
    loop.run_until_complete(process_as_results_come_in())
    print("\nNow, process results once they are all ready:")
    loop.run_until_complete(process_once_everything_ready())


if __name__ == '__main__':
    main()