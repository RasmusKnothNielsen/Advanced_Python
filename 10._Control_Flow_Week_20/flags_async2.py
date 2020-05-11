# file: flags_async2.py

import asyncio
import time

import requests

from flags import flag_list, show, save_flag


BASE_URL = 'http://cuda:8000'
SOURCE_DIR = 'w2560'
DEST_DIR = 'downloads/'


async def main():       # Declare as async, since we want to use it in the event loop
    t0 = time.time()
    futures = []
    for cc in flag_list():
        show(cc)
        url = f'{BASE_URL}/{cc}'
        futures.append(loop.run_in_executor(None, requests.get, url))
    for future in futures:
        response = await future
        save_flag(response.content, response.url.split('/')[-1])
    t1 = time.time() - t0
    print(f'\n{t1:.2f}sec')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())