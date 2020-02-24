# t= Timer()
# t('started up')
# t('something else')
# t('almost done')
# t() outputs the things with timestamp from the begining.

import time


class Timer:

    def __init__(self):
        self._time_stamps = []

    def __call__(self, *args):
        time_stamp = time.perf_counter_ns()
        if len(args) > 1:  # If more than one argument is given
            raise ValueError('Too many arguments provided, only one is supported!')
        if args:
            self._time_stamps.append((time_stamp, args[0]))
        else:
            last_timestamp = self._time_stamps[0][0] if self._time_stamps else 0
            delta_time_stamps = []
            for ts, label in self._time_stamps:
                delta_time_stamps.append((ts - last_timestamp, label))
                last_timestamp = ts
            return delta_time_stamps


if __name__ == "__main__":
    t = Timer()
    t('Started up')
    t('Something else')
    t('Almost done')
    # t('one', 'two')
    print(t())
