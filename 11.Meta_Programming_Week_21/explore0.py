# file: explore0.py
"""
Used to work with JSON on a more logical way.
Instead of using:
>>> feed['Schedule']['events'][40]['name']

with this, we can use:
>>> feed.Schedule.events[40].name
instead
"""
from collections import abc


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object using attribute notation"""

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
