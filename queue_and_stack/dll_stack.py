import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList as DBL


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.stack = DBL()

    def push(self, value):
        self.stack.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
        return self.stack.remove_from_tail()

    def __len__(self):
        return self.size
