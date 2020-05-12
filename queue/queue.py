"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue? Linked lists come with a built in fifo ordering to them,
   its very easy to impliment

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self, data=[]):
        self.size = 0
        self.length = len(data)
        self.storage = data

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.storage.append(value)
        self.length += 1

    def dequeue(self):
        if self.length >= 1:
            val = self.storage[0]
            self.storage.remove(self.storage[0])
            self.length -= 1
            return val
        else:
            return None
