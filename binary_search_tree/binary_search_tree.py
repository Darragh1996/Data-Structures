import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        newTree = BinarySearchTree(value)
        currentTree = self
        inserted = False
        while not inserted:
            if value >= currentTree.value:
                if currentTree.right == None:
                    currentTree.right = newTree
                    inserted = True
                else:
                    currentTree = currentTree.right
            else:
                if currentTree.left == None:
                    currentTree.left = newTree
                    inserted = True
                else:
                    currentTree = currentTree.left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right != None:
            return self.right.contains(target)
        elif target <= self.value and self.left != None:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        currentTree = self
        while currentTree.right != None:
            currentTree = currentTree.right
        return currentTree.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right != None:
            self.right.for_each(cb)
        if self.left != None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left != None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right != None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            print(current.value) 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.size > 0:
            current = s.pop()
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)
            print(current.value) 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node, s = Stack()):
        s.push(node)
        while s.size > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                self.pre_order_dft(current.left, s)
            if current.right:
                s.push(current.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node, s = Stack()):
        search = True
        while search:
            current = node
            if current.left != None:
                self.post_order_dft(current.left, s)
            if current.right != None:
                self.post_order_dft(current.right, s)
            s.push(node)
            search = False
        while s.size > 0:
            print(s.pop().value)