import unittest
from lru_doubly_linked_list import ListNode
from lru_doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1, 2)
        self.dll = DoublyLinkedList(self.node)

    def test_list_remove_from_tail(self):
        self.dll.remove_from_tail()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(1, 33)
        self.assertEqual(self.dll.head.value, 33)
        self.assertEqual(self.dll.tail.value, 33)
        self.assertEqual(self.dll.head.key, 1)
        self.assertEqual(self.dll.tail.key, 1)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 33)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(2, 68)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 68)
        self.assertEqual(len(self.dll), 0)

    def test_list_remove_from_head(self):
        self.dll.remove_from_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(2, 3)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.tail.value, 3)
        self.assertEqual(self.dll.head.key, 2)
        self.assertEqual(self.dll.tail.key, 2)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 3)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(4, 55)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 55)
        self.assertEqual(len(self.dll), 0)

    def test_list_add_to_tail(self):
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(self.dll.tail.key, 1)

        self.assertEqual(len(self.dll), 1)

        self.dll.add_to_tail(2, 30)
        self.assertEqual(self.dll.tail.prev.value, 2)
        self.assertEqual(self.dll.tail.prev.key, 1)
        self.assertEqual(self.dll.tail.key, 2)
        self.assertEqual(self.dll.tail.value, 30)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(3, 20)
        self.assertEqual(self.dll.tail.prev.value, 30)
        self.assertEqual(self.dll.tail.prev.key, 2)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(self.dll.tail.key, 3)
        self.assertEqual(len(self.dll), 3)

    def test_node_delete(self):
        node_1 = ListNode(1, 3)
        node_2 = ListNode(2, 4)
        node_3 = ListNode(3, 5)

        node_1.next = node_2
        node_2.next = node_3
        node_2.prev = node_1
        node_3.prev = node_2

        node_2.delete()

        self.assertEqual(node_1.next, node_3)
        self.assertEqual(node_3.prev, node_1)

    def test_node_insert_before(self):
        self.node.insert_before(1, 0)
        self.assertEqual(self.node.prev.value, 0)

    def test_list_add_to_head(self):
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.head.key, 1)

        self.dll.add_to_head(2, 10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.key, 2)
        self.assertEqual(self.dll.head.next.value, 2)
        self.assertEqual(self.dll.head.next.key, 1)

        self.assertEqual(len(self.dll), 2)

    def test_node_insert_after(self):
        self.node.insert_after(1, 2)
        self.assertEqual(self.node.next.value, 2)

    def test_list_move_to_end(self):
        self.dll.add_to_head(2, 40)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(self.dll.tail.key, 1)
        self.assertEqual(self.dll.head.value, 40)
        self.assertEqual(self.dll.head.key, 2)

        self.dll.move_to_end(self.dll.head)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.key, 2)
        self.assertEqual(self.dll.tail.prev.value, 2)
        self.assertEqual(self.dll.tail.prev.key, 1)

        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(3, 4)
        self.dll.move_to_end(self.dll.head.next)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.key, 2)
        self.assertEqual(self.dll.tail.prev.value, 4)
        self.assertEqual(self.dll.tail.prev.key, 3)
        self.assertEqual(len(self.dll), 3)

    def test_list_move_to_front(self):
        self.dll.add_to_tail(1, 3)
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.head.key, 1)

        self.assertEqual(self.dll.tail.value, 3)
        self.assertEqual(self.dll.tail.key, 1)

        self.dll.move_to_front(self.dll.tail)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.key, 1)

        self.assertEqual(self.dll.head.next.value, 2)
        self.assertEqual(self.dll.head.next.key, 1)

        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_head(3, 29)
        self.dll.move_to_front(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.key, 1)

        self.assertEqual(self.dll.head.next.value, 29)
        self.assertEqual(self.dll.head.next.key, 3)

        self.assertEqual(len(self.dll), 3)

    def test_list_delete(self):
        self.dll.delete(self.node)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(2, 5)
        self.dll.add_to_head(9, 3)
        self.dll.add_to_tail(6, 4)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 5)
        self.assertEqual(self.dll.head.key, 2)
        self.assertEqual(self.dll.tail.key, 6)
        self.assertEqual(self.dll.tail.value, 4)
        self.assertEqual(len(self.dll), 2)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.key, 6)
        self.assertEqual(self.dll.tail.key, 6)
        self.assertEqual(self.dll.tail.value, 4)
        self.assertEqual(self.dll.head.value, 4)

        self.assertEqual(len(self.dll), 1)

    def test_get_max(self):
        self.assertEqual(self.dll.get_max(), 2)
        self.dll.add_to_tail(2, 100)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(3, 55)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(4, 101)
        self.assertEqual(self.dll.get_max(), 101)


if __name__ == '__main__':
    unittest.main()
