"""
This module holds a Node class for working with a binary tree.

Classes: Node
"""

import math
import random


class Node:
    """ Binary tree node. A root node serves as an entry point for the tree.

    Tests:

    >>> root = Node(*[5, 1, 7, 8, 2, 3, 0, 9, 6])
    >>> root.__call__()
    [0, 1, 2, 3, 5, 6, 7, 8, 9]
    >>> root.insert([4])
    >>> root.__call__()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> root.remove(0)
    True
    >>> root.__call__()
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> root.remove(10)
    False
    >>> root.__call__()
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> root.insert([8, 4, 10])
    >>> root.__call__()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> rootStrings = Node(*["Fred", "William", "Tally"])
    >>> rootStrings.__call__()
    ['Fred', 'Tally', 'William']
    >>> rootStrings.insert(['S'])
    >>> rootStrings.insert(['s'])
    >>> rootStrings.__call__()
    ['Fred', 'S', 'Tally', 'William', 's']


    >>> root.insert(['a'])
    >>> root.__call__()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a']
    """

    # Removed value/values and using asterisk unpacking
    def __init__(self, *values):
        """ Class initializer.

        :param: values
            Can be one or several, using unpacking
        """
        counter = 0
        for value in values:
            self.left = None
            self.right = None
            self.value = value
            counter += 1
            if counter > 0:
                self.value = values[0]
                self.insert(values[1:])
            else:
                self.value = None

    def __repr__(self):
        return f"{self.value}"
        # return str(self.value)

    def __len__(self):
        """ Returns number of nodes in the binary tree.

        :return: Int
            Returns the size of the binary tree
        """
        return len(self.__call__())

    def __contains__(self, value):
        """ Checks if the value is already in the binary tree

        :param value:
            The value to be checked.

        :return: bool
            Returns true if tree contains value, else false."""

        return value in self.__call__()

    def insert(self, values):
        """ Insert value into tree.

        :param values:
            Can either be one or several values in a list
        """

        for value in values:
            if not self.__contains__(value):  # If the value is not in the tree
                if value < self.value:
                    if self.left:
                        self.left.insert([value])
                    else:
                        self.left = Node(value)
                else:
                    if self.right:
                        self.right.insert([value])
                    else:
                        self.right = Node(value)

    def remove(self, value):
        """ Remove element with value from tree.

        :param value:
            The value that is going to be removed.

        :return: bool
            Returns true if element is found, else false.
        """
        subtree = self.__call__()
        try:
            subtree.remove(value)
        except ValueError as error:
            print("ValueError Exception!", error.strerror)
        random.shuffle(subtree)
        self.left = None
        self.right = None
        if subtree:
            self.value = subtree.pop()
            self.insert(subtree)
        else:
            self.value = None
        return True

    # Changed from subtree to the dunder method __call__
    def __call__(self):
        """ Returns a sorted list when the object() is called.
        For example, node()

        :return: list
            Returns a list representation of the binary tree
        """
        if self.left:
            left = self.left.__call__()
        else:
            left = []
        if self.right:
            right = self.right.__call__()
        else:
            right = []
        return left + [self.value] + right

    def height(self):
        """ The height of the tree as understood in graph theory.
        """
        return self._max_depth() - 1

    def _max_depth(self):
        """ Helper function for calculating depth.
        """
        left_depth = self.left._max_depth() if self.left else 0
        right_depth = self.right._max_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def optimization_level(self):
        """ Gives a measure for how perfectly balanced the binary tree is. Range [0..1], where 1 is perfect.
        """
        return max(0, min(1, math.ceil(math.log2(len(self))) / self.height())) if self.height() > 0 else 0


if __name__ == '__main__':
    """
    Added testcases:
    - What happens if we input the same value several times? 
    - What happens if we remove something that is not in the tree?
    - What happens if we input chars into a tree with integers?
    - What happens if we input a lower case letter and a upper case letter in to a String Tree?
    
    Added __contains__ dunder method
    
    Changed subtree name to sorted_list, for a more pythonic description of the function
    
    Changed error handling in remove, so it returns true if item removed or else it returns false. No crashing.
    
    TODO:
    - Consider if it makes sense to implement __getitem__ method
    - What about __iter__() method?
    - Fix the error, when adding a str to an int tree. How to handle it?
    """

    import doctest

    doctest.testmod()

    list_of_numbers = [4, 8, 6]
    root = Node(*list_of_numbers)
    root.insert([9])
    print(root.__call__())
    root.insert([1, 5, 8, 10])
    print(root.__call__())

    print(root.__repr__())

    """ Showing how chars are being calculated """
    print("Int value of ASCII S: " + str(ord('S')))
    print("Int value of ASCII s: " + str(ord('s')))
    print("Int value of ASCII T: " + str(ord("T")))
    print("Int value of ASCII t: " + str(ord("t")))
    print(root())


