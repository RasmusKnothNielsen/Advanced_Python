# Notes from 3/2-2020

f string:
Nice way to put variables into a string.
> name = 'Rasmus'
>a = f"My name is {name}"


Tuples is atomical, which means that they are only done, if both can be done
> a, b = 42, 44
>
>a, b = b, a


For loops:
> for a in range(10):
>   print(a)

While loops
> while a < 3:
>   print("A is still less")
>   a += 1

Definition of functions

> def f("name"):
>   print(f"Hello, {name}")

It's also possible to return many different things
> def f():
>   return 42, 47
>
>a, b = f()
>
>a
>42
>
>b
>47

List comprehensions
> [i for i in range(2,8,2)]
>[2,4,6]
>
>[i for i in range(8) if i > 0 and i % 2 == 0]
>[2,4,6]

Generator object
If you dont know how many numbers you need, its better to use Generator objects
> (i for i in range(8) if i > 0 and i % 2 == 0)
> <generator object <genexpr> at 0x109e38b30>

Dictionaries
Very quick to get things from, since it's nearly instantanious.
Uses a hash function to save and find the key
> d = {"name": "Rasmus", "color": "Orange"}
>d["name"]
>"Rasmus"

Set
There are no duplicates in a set
Very effective to get rid of duplicates in a list, turn a list into a set and back into a list.
This would be done, if mutability is important.
> s = set([1,2,2,3,3])
>s is equal to [1,2,3]

