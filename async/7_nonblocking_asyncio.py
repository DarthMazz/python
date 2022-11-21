import asyncio
import aiohttp
import time


async def fetch(session, url):
    async with session.get(url) as response:
        response = await response.read()
        return response


async def fetch_many(host, paths_todo):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [fetch(session, host + path) for path in paths_todo]
        responses = await asyncio.gather(*tasks)
        return responses


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    host = 'http://example.com'
    paths_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}
    elapsed_times = 0
    for _ in range(10):
        start = time.time()
        loop.run_until_complete(fetch_many(host, paths_todo))
        elapsed_time = time.time() - start
        elapsed_times += elapsed_time
        print(f"elapsed_time: {(elapsed_time):.2f}[sec]")
    print(f"mean_elapsed_time: {(elapsed_times/10):.2f}[sec]")