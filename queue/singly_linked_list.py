class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def add_next(self, node):
        self.next = node


class LinkedList():
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        if self.tail:
            self.tail.next = None
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return SllIterator(self)

    def add_to_head(self, value):
        '''this method is not tested'''
        new = ListNode(value)
        if self.head == None:
            self.head = new
            self.tail = new
            self.tail.next = None
            self.length += 1
        else:
            new.next = self.head
            self.head = new
            self.length += 1

    def remove_head(self):
        if self.head != None:
            val = self.head.value
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return val
        else:
            return None

    def add_to_tail(self, value):
        if self.tail != None:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.head = ListNode(value)
            self.tail = self.head
            self.tail.next = None
            self.length += 1

    def contains(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_max(self):
        if self.head == None:
            return None
        current = self.head
        max = self.head.value
        while current != None:
            if current.value > max:
                max = current.value
            current = current.next
        return max

    def print_list(self):
        if self.head == None:
            print(None)
            return None
        current = self.head
        while current != None:
            print(current)
            current = current.next
