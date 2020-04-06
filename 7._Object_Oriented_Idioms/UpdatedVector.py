"""
@Author: Rasmus Knoth Nielsen
Advanced Python course
4. Semester, AP in Computer Science, KEA, Denmark
"""
from array import array
import reprlib
import math


class Vector:
    """
      >>> v = Vector([1, 2, 3, 4])
      >>> list(v)
      [1.0, 2.0, 3.0, 4.0]
      >>> v2 = Vector((1, 2))
      >>> list(v2)
      [1.0, 2.0]

      >>> v3 = Vector([3,4,5])
      >>> len(v3)
      3

      >>> v4 = Vector(range(7))
      >>> v4[1:4]
      Vector([1.0, 2.0, 3.0])

      >>> v5 = Vector(range(5))
      >>> v5.x, v5.y, v5.t
      (0.0, 1.0, 3.0)
   """

    typecode = 'd'

    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return id(self)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers.')

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        raise AttributeError(f'{cls.__name__} object has no attribute {name}')

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = f'Attribute {name} is read only.'
            elif name.islower():
                error = "Can't set attribute names 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

    v1 = Vector(range(5))
    v2 = Vector(range(10))

    print(hash(v1))
    print(hash(id(v2)))

