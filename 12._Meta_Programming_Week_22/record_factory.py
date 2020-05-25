def record_factory(cls_name, field_names):
    """
    >>> Dog = record_factory('Dog', 'name weight owner')
    >>> rex = Dog('Rex', 30, 'Bob')
    >>> rex
    Dog(name='Rex', weight=30, owner='Bob')
    >>> name, weight, _ = rex
    >>> name, weight
    ('Rex', 30)
    >>> "{2}'s dog weighs {1}kg".format(*rex)
    "Bob's dog weighs 30kg"
    >>> rex.weight = 32
    >>> rex
    Dog(name='Rex', weight=32, owner='Bob')
    >>> Dog.__mro__
    (<class '__main__.Dog'>, <class 'object'>)
    """
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError: # no .replace or .split
        pass # assume it's already a sequence of identifiers
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return f'{self.__class__.__name__}({values})'

    cls_attrs = dict(__slots__ = field_names,
                    __init__ = __init__,
                    __iter__ = __iter__,
                    __repr__ = __repr__)

    return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()