"""
An implementation of a Vector in 2D space,
Complete with tests and docstrings

"""
from math import hypot


class Vector:

    def __init__(self, x, y):
        """
        Initializing the Vector object

        :param x: int
            Defines the place on the x axis

        :param y: int
            Defines the place on the y axis
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Method that adds two vectors together an returns a new vector with the product

        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)

        :param other: Vector
            The Other vector that we want to add to the vector the method is called upon.

        :return: Vector
            Returns the new vector that represents the product of the two vectors
        """
        new_vector = Vector(self.x + other.x, self.y + other.y)
        return new_vector

    def __sub__(self, other):
        """
        Method that subtracts a vector with another, by subtracting the x values with each other and the y values
        and subtracting it with each other.
        :param other:
        :return:
        """
        new_vector = Vector(self.x - other.x, self.y - other.y)
        return new_vector

    def __abs__(self):
        """
        Method that returns the absolute of a vector

        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0

        :return: int
            The computed absolute value of the vector
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """

        >>> True if Vector(0, 0) else False
        False
        >>> True if Vector(1, 0) else False
        True

        :return:
        """
        return bool(abs(self))


    def __repr__(self):
        """
        Method to return a representation of the Vector as a string

        :return: String
            A string representation of the vector, the method has been called upon.
        """
        return "Vector(%r, %r)" % (self.x, self.y)

    def __mul__(self, scalar):
        """

        Method to extending a vector with the given scalar value.
        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        >>> abs(v * 3)
        15.0

        :param scalar: int
            The value that we want to multiply the values with, to extend the vector

        :return: Vector
            Returning a new vector that has been extended with the given scalar value.
        """
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    # Import and run the doctest if the class is run as main
    import doctest
    doctest.testmod()
