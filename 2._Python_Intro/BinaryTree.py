""" Assignment 1: Implement a binary tree.
    - The tree is initialized with a sequence of elements, maybe empty
    - The tree can return an sorted list of elements
    - The tree supports insertion of new elements
    - The tree supports deletion of elements

    Remember:
    - Document your code
    - DRY
    - Separate configuration from implementation
    - Single Responsibility Principle
    - Test the code
    """

# import testmod for testing our functionality
from doctest import testmod


class Node:
    """
    Defining the Node class
    """

    def __init__(self, *value):
        """
        Initializing method that creates the binary tree and fills it with value(s)

        >>> root = Node(10)
        >>> root.print_tree()
        [10]

        >>> root = Node(*[4,6,2,8])
        >>> root.print_tree()
        [[2], 4, [6, [8]]]


        :param value: int or list
            an integer or a list of integers that are going to be added to the binary tree

        :return: Node
            Returns itself, so that it can be saved to a variable.
        """
        i = 0
        for number in value:
            if i == 0:  # If this is the first Node
                self.left = None
                self.right = None
                self.data = number
                i += 1
            else:  # If there already is a node
                self.insert(number)

    # Method that inserts data into the right place in the Binary Tree
    # Using * to unpack the values coming in from the function call
    def insert(self, *data):
        """
        Method that inserts data into the right place in a Binary Tree.

        It is using the * syntax, which allows for unpacking of values,
        if a list of values are provided at method call.

        >>> root = Node(4)
        >>> root.insert(2)
        >>> root.print_tree()
        [[2], 4]

        >>> root = Node(*[6,3,9])
        >>> root.insert(5)
        >>> root.print_tree()
        [[3, [5]], 6, [9]]

        :param data: Single value or list of values
            The value og the list of values that we want to insert into the binary tree

        :return: void
            Nothing is returned, but the binary tree that the method is executed on is modified.
        """
        # Since we are unpacking values, we have to take the values one at a time
        for number in data:
            # Compare the new value with the parent node
            if self.data:
                if number < self.data:  # If number is smaller than the current node
                    if self.left is None:
                        self.left = Node(number)
                    else:
                        self.left.insert(number)
                elif number > self.data:  # If number is larger than the current node
                    if self.right is None:
                        self.right = Node(number)
                    else:
                        self.right.insert(number)
            else:
                self.data = number

    def delete_node(self, *data):
        """
        This method deletes the provided value(s) in the binary tree that it is called upon.

        >>> root = Node(*[4,7,9,1])
        >>> root.delete_node(7)
        >>> root.print_tree()
        [[1], 4, [9]]

        >>> root = Node(*[5,8,3,1,6,9,7,10])
        >>> root.delete_node(*[8,6,9])
        >>> root.print_tree()
        [[[1], 3], 5, [[7], 10]]

        :param self: Node
            The binary tree on which we want to delete a node from.

        :param data: value(s)
            A value or list of values that we want to delete from the binary tree

        :return: Node
            The function returns the binary tree without the deleted nodes.
        """
        for number in data:
            # Base Case
            if self is None:
                return self

            # If the key to be deleted is smaller than the root's
            # key then it lies in  left subtree
            if number < self.data:
                self.left = self.left.delete_node(number)

            # If the kye to be delete is greater than the root's key
            # then it lies in right subtree
            elif number > self.data:
                self.right = self.right.delete_node(number)

            # If key is same as root's key, then this is the node
            # to be deleted
            else:

                # Node with only one child or no child
                if self.left is None:
                    temp = self.right
                    return temp

                elif self.right is None:
                    temp = self.left
                    return temp

                # Node with two children: Get the in order successor
                # (smallest in the right subtree)
                temp = min_value_node(self.right)

                # Copy the in order successor's content to this node
                self.data = temp.data

                # Delete the in order successor
                self.right = self.right.delete_node(temp.data)

        return self

    def print_tree(self):
        """
        Method to print the tree in chronological order

        :return: list
            Returns a list of numbers that represents the binary tree
        """
        result = []
        if self.left:
            result.append(self.left.print_tree())
        result.append(self.data)
        if self.right:
            result.append(self.right.print_tree())
        return result


# Given a non-empty binary search tree, return the node
# with minimum key value found in that tree. Note that the
# entire tree does not need to be searched
def min_value_node(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


if __name__ == '__main__':

    # Enable the test module
    testmod(name='__init__.Node', verbose=True)

    # Create a list of numbers to feed into the insert method
    list_of_numbers = [5, 2, 6, 9, 3, 1, 65, 23]

    # Initialize the tree with a list of numbers
    print("Creating binary tree with a list of numbers")
    root = Node(*list_of_numbers)
    print(root.print_tree())
    print()

    # Insert a single value
    print("Inserting single values into the binary tree")
    root.insert(70)
    root.insert(10)
    print(root.print_tree())
    print()

    # Insert another list into the binary tree
    print("Inserting another list into the binary tree")
    new_list_of_numbers = [4, 14, 27, 51]
    root.insert(*new_list_of_numbers)
    print(root.print_tree())
    print()

    # Deletes a single value
    print("Deletes a single value from the binary tree")
    root.delete_node(5)
    print(root.print_tree())
    print()

    # Deletes a list of values
    print("Deletes a list of values from the binary tree")
    delete_numbers = [3, 9, 65]
    root.delete_node(*delete_numbers)
    print(root.print_tree())
