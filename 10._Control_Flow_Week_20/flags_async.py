# file: flags_async.py

import asyncio
import time

import requests

from flags import flag_list, show, save_flag


BASE_URL = 'http://cuda:8000'
SOURCE_DIR = 'w2560'
DEST_DIR = 'downloads/'


async def download_one(cc):
    show(cc)
    url = f'{BASE_URL}/{cc}'
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    save_flag(response.content, cc)

async def main():
    t0 = time.time()
    for cc in flag_list():
        await download_one(cc)
    t1 = time.time() - t0
    print(f'\n{t1:.2f}sec')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())