class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Append
    def append(self, value):
        count = len(self)
        current_node = self.head
        for i in range(count - 1):
            current_node = current_node.next
        current_node.next = Node(value)

    # Extend
    def extend(self, list):
        for number in list:
            self.append(number)

    # Insert
    def insert(self, index, value):
        current_node = self.head
        if index == 0:
            pointer_to_list = self.head
            self.head = Node(value)
            self.head.next = pointer_to_list
        else:
            count = 0
            while count < index - 1:
                current_node = current_node.next
                count += 1
            pointer_to_link = current_node.next
            current_node.next = Node(value)
            current_node.next.next = pointer_to_link

    # Remove
    def remove(self, value):
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
        if current_node.next is None:
            raise ValueError("Value is not present in the Linked List")

    # Pop
    def pop(self, index):
        if (index is not None):
            if index >= len(self):
                raise IndexError("Index out of bounds!")
            current_node = self.head
            count = 0
            while count < index - 1:
                current_node = current_node.next
                count += 1
            value = current_node.next.data
            current_node.next = current_node.next.next
            return value
        else:
            print("Index is none")
            count = 0
            length = len(self)
            current_node = self.head
            while count < length:
                current_node = current_node.next
            value = current_node.next.value
            current_node.next = None
            return value

    # Clear
    def clear(self):
        self.head = None

    # Index
    def index(self, value):
        count = 0
        current_node = self.head
        while current_node.data is not value:
            current_node = current_node.next
            count += 1
        return count

    # Count
    def count(self, data):
        count = 0
        current_node = self.head
        if current_node.data == data:
            count += 1
        while current_node.next is not None:
            if current_node.next.data == data:
                count += 1
            current_node = current_node.next

        return count

    # Sort?
    def sort(self):
        list = self.asList()
        list.sort()
        self.head = Node(list.pop(0))
        for number in list:
            self.append(number)

    # Reverse?
    def reverse(self):
        list = self.asList()
        list.reverse()
        self.head = Node(list.pop(0))
        for number in list:
            self.append(number)

    # Copy
    def __copy__(self):
        pass

    # As List
    def asList(self):
        list = []
        current_node = self.head
        for i in range(len(self)):
            list.append(current_node.data)
            current_node = current_node.next
        return list

    # Length
    def __len__(self):
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


