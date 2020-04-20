class DoppelDict(dict):

    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, item):
        return self._data[item]

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        count = 0
        for key in self._data:
            count += 1
        return count

    def __contains__(self, item):
        flag = False
        for key in self._data:
            if key == item:
                flag = True
        return flag

    def __iter__(self):
        self._count = 1
        return self

    def __next__(self):
        x = self._count
        self._count += 1
        return x