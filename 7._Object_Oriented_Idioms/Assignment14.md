# Assignment 14

What are the pros and cons for using any of these data structures as underlying data structures for a vector class:

    list

    dict

    tuple

    set

Implement the two most suitable.

### List
List is a collection of ordered and mutable elements. Lists allow duplicates.

### Dictionary
Dictionary is a collection that is unordered, mutable and indexed (with a key).  
We can not be sure about what order the entries comes in.

### Tuple
Tuples is immutable and ordered, so as long as we do not want to change anything in our vectors, we can use tuples.  
Tuples also support duplicates.

### Set
Set is immutable, unique and unorderet, which could be a hindrance for our vector class


Since it would be a good idea to be able to hold duplicates, it would be a good idea to implement List and Tuple.  
Using tuples when we need the vectors to be immutable and Lists when we need them to be mutable.

