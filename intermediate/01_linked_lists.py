# 01_linked_lists.py
#
# A linked list stores values in nodes. Each node points to the next node.
# Python lists are usually better in real code, but linked lists teach references.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


numbers = LinkedList()
numbers.append(10)
numbers.append(20)
numbers.append(30)

print("Linked list values:", numbers.to_list())
print("Contains 20?", numbers.contains(20))
print("Contains 99?", numbers.contains(99))
