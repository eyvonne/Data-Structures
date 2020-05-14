"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, key, value):
        current_next = self.next
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def __str__(self):
        return f'key: {self.key}, value: {self.value}'

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def get_value(self):
        return self.value

    def set_value(self, key, value):
        self.key = key
        self.value = value

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return DllIterator(self)
    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, key,  value):
        new = ListNode(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new
            self.tail = new
        else:
            new.set_next(self.head)
            self.head.set_prev(new)
            self.head = new

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
# this will use the new and improved delete function

    def remove_from_head(self):
        return_val = self.head.value
        self.delete(self.head)
        return return_val

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, key, value):
        if self.length >= 1:
            self.tail.insert_after(key, value)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(key, value)
            self.head = self.tail
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
# this will use the new and improved delete function

    def remove_from_tail(self):
        return_val = self.tail.value
        self.delete(self.tail)
        return return_val

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
# this will use the new and improved delete method

    def move_to_front(self, node):
        self.delete(node)
        node.set_next(self.head)
        self.head.set_prev(node)
        self.head = node
        self.length += 1

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
# this will use the new and improved delete method

    def move_to_end(self, node):
        self.delete(node)
        node.set_prev(self.tail)
        self.tail.set_next(node)
        self.tail = node
        self.length += 1

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.get_key(node.key):
            if self.head == self.tail:
                if node == self.head:
                    self.head = None
                    self.tail = None
            elif self.head == node:
                self.head.next.set_prev(None)
                self.head = self.head.next
            elif self.tail == node:
                self.tail.prev.set_next(None)
                self.tail = self.tail.prev
            else:
                node.delete()
            self.length -= 1
        else:
            return None
    """Returns the highest value currently in the list"""

    def get_max(self):
        max = self.head.value
        current = self.head
        while current != None:
            if current.value > max:
                max = current.value
            current = current.next
        return max

    def print_list(self):
        current = self.head
        while current != None:
            print(current)
            current = current.next

    def check_key(self, key):
        keys = [node.key for node in self]
        if key in keys:
            return True
        else:
            return False

    def get_key(self, key):
        '''finds the node with the given key and returns it'''
        for node in self:
            if node.key == key:
                return node

# this class makes the Doubly linked list iterable


class DllIterator:
    def __init__(self, dll):
        self._dll = dll
        self._index = 0

    def __next__(self):
        if self._index < len(self._dll):
            node = self._dll.head
            for i in range(self._index):
                node = node.next
            self._index += 1
            return node
        raise StopIteration


if __name__ == '__main__':
    dll = DoublyLinkedList(ListNode(2, 2))
    dll.add_to_head(2, 2)
    dll.add_to_head(3, 2)
    dll.add_to_head(4, 2)
    dll.add_to_tail('a', 'tail')
    dll.add_to_tail(5, 'tail2')
    dll.add_to_tail(6, 'tail3')
    print(dll.check_keys())
