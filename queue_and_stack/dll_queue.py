import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList as DBL


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.queue = DBL()

    def enqueue(self, value):
        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        return self.queue.remove_from_head()

    def len(self):
        return self.size
