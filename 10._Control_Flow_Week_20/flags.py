# file: flags.py

import os
import time
import sys

import requests


BASE_URL = 'http://localhost:8000'
#BASE_URL = 'http://192.168.51.76:8000'
SOURCE_DIR = 'w2560/'
DEST_DIR = 'downloads/'

def flag_list():
    return [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = f'{BASE_URL}/{cc}'
    response = requests.get(url)
    return response.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, f'{cc.lower()}')
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(flag_list())
    t1 = time.time() - t0
    print(f'\n{count} flags downloaded in {t1:.2f}sec.')

if __name__ == '__main__':
    main(download_many)
