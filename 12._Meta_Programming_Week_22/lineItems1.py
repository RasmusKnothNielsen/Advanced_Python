"""
If you make an instance walnuts = LineItem(‘walnuts’, 10, 20) and take a look at it with dir(walnuts)
you will see that the managed instances are stored as _Quantity#0 and _Quantity#1
even though these are not valid identifier names you would normally be able to assign,
but with setattr this is possible.

While it works nicely from the managed class, this is not a very nice implementation. Nevertheless,
what we have done here is the same as what ORMs such as the Django ORM and SQL Alchemy are doing;
if we moved the Quantity class to mondels.py we would have something like price = models.Quantity() -
just as you will find in many frameworks. In fact,
this kind of programming would usually not be part of smaller project,
but large projects and frameworks, where intensive reuse of the code makes it worth while,
the separation and abstraction we achieve is well worth the effort.
It is also very useful to know how this works when you are using such components from frameworks.
"""

class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}'
        cls.__counter += 1

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price