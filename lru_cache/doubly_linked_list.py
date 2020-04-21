"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, key, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value, key):
        new_head = ListNode(value, key, None, self.head)
        if self.head == None:
            self.head = self.tail = new_head
        else:
            self.head.prev = new_head
            self.head = new_head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head:
            value = self.head.value
            self.head.delete()
            if self.head == self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
            if self.length > 0:
                self.length -= 1
            return value
        else:
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value, key):
        new_tail = ListNode(value, key, self.tail, None)
        if new_tail.prev != None:
            self.tail.next = new_tail
        else:
            self.head = new_tail
        self.tail = new_tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail:
            key = self.tail.key
            self.tail.delete()
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.prev
            if self.length > 0:
                self.length -= 1
            return key
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node != None:
            if node == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            node.delete()
            self.head.prev = node
            node.next = self.head
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node != None:
            if node == self.head:
                self.head = self.head.next
                self.head.prev = None
            node.delete()
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if node == None:
        #     pass
        if node == self.head or node == self.tail:
            if node == self.head:
                new_head = self.head.next
                self.head.delete()
                self.head = new_head
            if node == self.tail:
                self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        current = self.head
        maxValue = self.head.value
        while current.next != None:
            if current.next.value > maxValue:
                maxValue = current.next.value
            current = current.next
        return maxValue
