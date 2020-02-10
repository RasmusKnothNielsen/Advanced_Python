""" Assignment 1: Implement a binary tree.
    - The tree is initialized with a sequence of elements, maybe empty
    - The tree can return an sorted list of elements
    - The tree supports insertion of new elements
    - The tree supports deletion of elements

    Remember:
    - Document your code
    - DRY
    - Seperate configuration from implementation
    - Sigle Responsibility Principle
    - Test the code
    """


# Define the Node
class Node:
    """Class that emulates a Binary Tree with insert and delete functions

    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    # Method that inserts data into the right place in the Binary Tree
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
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


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, data):
    # Base Case
    if root is None:
        return root

        # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if data < root.data:
        root.left = deleteNode(root.left, data)

        # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif data > root.data:
        root.right = deleteNode(root.right, data)

        # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = min_value_node(root.right)

        # Copy the inorder successor's content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root


if __name__ == '__main__':
    root = Node(10)
    root.insert(4)
    root.insert(12)
    root.insert(2)
    root.insert(3)
    root.insert(15)
    root.insert(13)
    root.insert(1)

    root = deleteNode(root, 2)

    print(root.print_tree())

    list_of_numbers = [5, 2, 6, 9, 3, 1, 65, 23]
    print(list_of_numbers.pop())
    print(list_of_numbers)