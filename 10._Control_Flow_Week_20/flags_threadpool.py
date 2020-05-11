# file: flags_threadpool.py

from concurrent import futures

from flags import save_flag, get_flag, show, main, flag_list


MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower())
    return cc

def download_many():
    workers = min(MAX_WORKERS, len(flag_list()))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(flag_list()))
    return len(list(res))

if __name__ == '__main__':
    download_many()