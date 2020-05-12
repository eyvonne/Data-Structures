"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
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

    def __str__(self):
        return f'value: {self.value}'

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

    def __iter__(self):
        return DllIterator(self)
    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.length >= 1:
            self.head = ListNode(value, next=self.head)
            self.length += 1
        elif self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        return_val = self.head.value
        if self.length > 1:
            self.head = self.head.next
            self.head.prev = None
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        self.length -= 1
        return return_val

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.length >= 1:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        return_val = self.tail.value
        if self.length > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        self.length -= 1
        return return_val

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        node.delete()
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.head == node:
            self.head = self.head.next

        node.delete()
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length > 2:
            if self.head == node:
                self.head = self.head.next
            if self.tail == node:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node.delete()
        elif self.length == 2:
            if self.head == node:
                self.head = self.tail
            else:
                self.tail = self.head
        elif self.length == 1:
            self.head = None
            self.tail = None
        self.length -= 1

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
    dll = DoublyLinkedList(ListNode(1))
    dll.add_to_head(2)
    dll.add_to_head(3)
    dll.add_to_head(4)
    dll.add_to_tail('tail')
    dll.add_to_tail('tail2')
    dll.add_to_tail('tail3')
    for i, node in enumerate(dll):
        print(i, node)
    print(*dll)
