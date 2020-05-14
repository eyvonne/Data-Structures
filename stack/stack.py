"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, value):
        self.storage.insert(0, value)
        self.length += 1

    def pop(self):
        if self.length >= 1:
            val = self.storage[0]
            self.storage.remove(val)
            self.length -= 1
            return val
        else:
            return None


class LLStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, value):
        self.storage.add_to_head(value)
        self.length += 1

    def pop(self):
        if self.length >= 1:
            val = self.storage.remove_head()
            self.length -= 1
            return val
        else:
            return None
