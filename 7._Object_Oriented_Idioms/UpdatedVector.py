"""
@Author: Rasmus Knoth Nielsen
Advanced Python course
4. Semester, AP in Computer Science, KEA, Denmark
"""
import numbers
from array import array
import reprlib
import math
import functools
import operator
import time


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

      >>> v6 = Vector(range(5))
      >>> v7 = Vector([0, 1, 2, 3, 5])
      >>> hash(v6) != hash(v7)
      True
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

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __eq__(self, other):
        if not len(self) == len(other):
            return False
        for a, b in zip(self, other):
            if not a == b:
                return False
        return True

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)

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
    v3 = Vector([0, 1, 2, 3, 5])

    # How to hash.
    # Either by doing a direct hash on the id of the object
    print("Hash of v1 via id():", hash(id(v1)))
    print("Hash of v2 via id():", hash(id(v2)))
    # Or by implementing xor hashing functionality
    print("Hash of v1 with created hash function:", hash(v1))
    print("Hash of v2 with created hash function:", hash(v2))
    print("Hash of v3 with created hash function:", hash(v3))

    # Performance tests
    listOfVectors = []
    number_list = [x for x in range(10000)]
    for i in range(1000):
        sequence = number_list[0:len(number_list):i+1]
        vector = Vector(sequence)
        listOfVectors.append(vector)

    listOfResults = []
    for i in range(100):
        start = time.time()
        for j in range(len(listOfVectors)-1):
            listOfVectors[j] == listOfVectors[j+1]
        end = time.time()
        listOfResults.append(end-start)
    print(sum(listOfResults)/100)

