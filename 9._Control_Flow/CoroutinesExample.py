from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    yield Result(count, average)


if __name__ == '__main__':

    coro_avg = averager()

    coro_avg.send(None)

    coro_avg.send(5)

    coro_avg.send(7)
    print(coro_avg.send(None))


