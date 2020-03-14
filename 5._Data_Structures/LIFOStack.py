class LIFOStack:

    def __init__(self):
        self._list = []

    # Append / Push
    def push(self, data):
        """
        Function to add an element at the top of a stack

        :param data:
            Data to be inserted at the top of the stack

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.push(7)
        >>> stack.push(9)
        >>> print(stack)
        [4, 7, 9]
        """
        self._list.append(data)

    # Pop
    def pop(self):
        """
        Function to remove an element at the top of a stack

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.push(7)
        >>> stack.push(9)
        >>> stack.pop()
        >>> print(stack)
        [4, 7]
        """
        self._list.pop()

    # Peek?
    def peek(self):
        """
        Function to peek at the top element without removing it.

        :return:
            The element at the top of the stack

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.push(7)
        >>> stack.push(9)
        >>> print(stack.peek())
        9
        >>> print(stack)
        [4, 7, 9]
        """
        return self._list[len(self) - 1]

    # Empty
    def empty(self):
        """

        :return:

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.empty()
        False
        >>> stack.pop()
        >>> stack.empty()
        True
        """
        return len(self) == 0

    # Extend

    # Count?
    def __len__(self):
        """
        Function that calculates the height of the stack

        :return: Int
            Height of stack

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.push(7)
        >>> stack.push(9)
        >>> print(len(stack))
        3
        """
        return len(self._list)

    # Clear?
    def clear(self):
        """
        Function that clears the stack, removing all elements.

        >>> stack = LIFOStack()
        >>> stack.push(4)
        >>> stack.push(7)
        >>> stack.push(9)
        >>> stack.clear()
        >>> print(stack)
        []
        """
        self._list = []

    # Copy?

    # Str
    def __str__(self):
        return self._list.__str__()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    stack = LIFOStack()
    stack.push(5)
    stack.push(7)
    print(stack)
    stack.push(10)
    stack.push(20)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack)
    stack.push("hi")
    print(stack)
    #stack.pop(0)
