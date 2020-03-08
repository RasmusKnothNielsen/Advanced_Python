class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Function that adds a node at the end of the linkedlist

        :param data:
            Data that is going to be added to the node
        """
        count = len(self)
        current_node = self.head
        for i in range(count - 1):
            current_node = current_node.next
        current_node.next = Node(data)

    def extend(self, elements):
        """
        Function that takes a list and adds it in the end of the linkedlist as nodes.

        :param elements:
            list of elements
        """
        for element in elements:
            self.append(element)

    def insert(self, index, data):
        """
        Function that inserts a node at a specific index

        :param index: Int
            Where to insert the node.
        :param data:
            What the node.data is going to contain
        """
        current_node = self.head
        if index == 0:
            pointer_to_list = self.head
            self.head = Node(data)
            self.head.next = pointer_to_list
        else:
            count = 0
            while count < index - 1:
                current_node = current_node.next
                count += 1
            pointer_to_link = current_node.next
            current_node.next = Node(data)
            current_node.next.next = pointer_to_link

    def remove(self, data):
        """
        Function that removes the first node with the provided data

        :param data:
            The data that is going to be searched for
        """
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
        if current_node.next is None:
            raise ValueError("Value is not present in the Linked List")

    def pop(self, index):
        """
        Function that removes and returns the data at the data at the given index.

        If no index is given, the last node is removed and returned.

        :param index: Int
            The given index that the user wants to remove and return.
        :return:
            The data inside the removed node.
        """
        if index is not None:
            if index >= len(self):
                raise IndexError("Index out of bounds!")
            current_node = self.head
            count = 0
            while count < index - 1:
                current_node = current_node.next
                count += 1
            data = current_node.next.data
            current_node.next = current_node.next.next
            return data
        else:
            print("Index is none")
            count = 0
            length = len(self)
            current_node = self.head
            while count < length:
                current_node = current_node.next
            data = current_node.next.value
            current_node.next = None
            return data

    def clear(self):
        """
        Function that clears the linked list
        """
        self.head = None

    def index(self, data):
        """
        Function that finds the index of the given data and returns the index

        :param data:
            The data that we are looking for the index of.
        :return: Int
            The index of the data that we are looking for.
        """
        count = 0
        current_node = self.head
        while current_node.data is not data:
            current_node = current_node.next
            count += 1
        return count

    def count(self, data):
        """
        Function that counts the occurrence of nodes with the given data in it.

        :param data:
            The element that we are looking for.
        :return: Int
            The number of times the given element is present in the linked list.
        """
        count = 0
        current_node = self.head
        if current_node.data == data:
            count += 1
        while current_node.next is not None:
            if current_node.next.data == data:
                count += 1
            current_node = current_node.next

        return count

    def sort(self):
        """
        Function that sorts all the elements in the linked list and rebuilds it in chronological order.
        """
        list = self.asList()
        list.sort()
        self.head = Node(list.pop(0))
        for number in list:
            self.append(number)

    def reverse(self):
        """
        Function that reverses the order of the nodes in the linked list.
        """
        list = self.asList()
        list.reverse()
        self.head = Node(list.pop(0))
        for number in list:
            self.append(number)

    # Copy
    def __copy__(self):
        pass

    def asList(self):
        """
        Function that returns the linked list as a regular list.

        :return:
            List of the data from the linked list.
        """
        list = []
        current_node = self.head
        for i in range(len(self)):
            list.append(current_node.data)
            current_node = current_node.next
        return list

    def __len__(self):
        """
        Function that returns the number of nodes in the linked list.

        :return: Int
            Number of nodes in the linked list.
        """
        count = 0
        current_node = self.head
        if current_node is None:
            return 0
        else:
            count += 1
            while current_node.next is not None:
                count += 1
                current_node = current_node.next
            return count

    def __str__(self):
        """
        Function that returns a string based on a human readable representation of the linked list

        :return: String
            A string representation of the linked list.
        """
        list = []
        current_node = self.head
        while (current_node):
            list.append(current_node.data)
            current_node = current_node.next
        return str(list)


if __name__ == "__main__":

    llist = LinkedList()
    llist.head = Node(4)
    llist.head.next = Node(6)
    llist.append(2)
    print(llist)
    llist.insert(2, 7)
    print(llist)
    llist.remove(6)
    print(llist)
    print(llist.index(7))
    print(llist.pop(1))
    llist.append(2)
    print("Count of 8: " + str(llist.count(8)))
    list = [9, 3, 13]
    llist.extend(list)
    print(llist)

    print("Converted to list")
    print(llist.asList())

    llist.sort()
    print("Sorted list:")
    print(llist)

    llist.reverse()
    print("Reversed")
    print(llist)

    llist.__copy__()


