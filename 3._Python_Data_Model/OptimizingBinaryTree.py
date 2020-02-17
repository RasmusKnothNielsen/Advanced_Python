"""
This module holds a Node class for working with a binary tree.

Classes: Node
"""

import math
import random


class Node:
    """ Binary tree node. A root node serves as an entry point for the tree.
    >>> root = Node(*[5, 1, 7, 8, 2, 3, 0, 9, 6])
    >>> root.sorted_list()
    [0, 1, 2, 3, 5, 6, 7, 8, 9]
    >>> root.insert([4])
    >>> root.sorted_list()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> root.remove(0)
    >>> root.sorted_list()
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    # Removed value/values and using asterisk unpacking
    def __init__(self, *values):
        """ Class initializer.
        Arguments: value = object | values = sequence of objects.
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
        """
        return len(self.sorted_list())

    def insert(self, values):
        """ Insert value into tree.
        """
        for value in values:
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
        """
        subtree = self.sorted_list()
        try:
            subtree.remove(value)
        except ValueError:
            raise ValueError(f'Tree does not contain {value}.')
        random.shuffle(subtree)
        self.left = None
        self.right = None
        if subtree:
            self.value = subtree.pop()
            self.insert(subtree)
        else:
            self.value = None

    # Changed from subtree to sorted_list
    def sorted_list(self):
        """ Sorted list of elements.
        """
        if self.left:
            left = self.left.sorted_list()
        else:
            left = []
        if self.right:
            right = self.right.sorted_list()
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
    import doctest

    doctest.testmod()

    list_of_numbers = [4, 8, 6]
    root = Node(*list_of_numbers)
    root.insert([9])
    print(root.sorted_list())

    print(root.__repr__())

    

