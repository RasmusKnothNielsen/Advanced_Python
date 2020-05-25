# file: osconfeed.py

from urllib.request import urlopen
import warnings
import os
import json


URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        warnings.warn(f'downloading {URL} to {JSON}.')
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


if __name__ == '__main__':
    load()
