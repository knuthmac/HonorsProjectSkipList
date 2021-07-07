"""
for honors project
CSE 331 S21 (Onsay)
Macinze Knuth
tests.py
"""

from HonorsProject.skiplist import Skip, Node
from typing import TypeVar, List
import random
import unittest


# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")            # represents generic type


class SLTests(unittest.TestCase):


    def test_insert(self):

        # (1) insert single node
        skip = Skip()
        skip.insert(2)
        self.assertIs(skip.head.next[0].value, 2)  # if failure here, see (1).

        # (2) insert single node on front
        skip.insert(0)
        self.assertIs(skip.head.next[0].value, 0)

        # (3) push multiple nodes on back
        skip = Skip()
        lst = []
        for i in range(5):
            skip.insert(i)
            lst.append(i)
        expected = skip.to_list()
        self.assertEqual(lst, expected)  # if failure here, see (3)

        # (4) pushing with more Nodes
        skip = Skip()
        lst = []
        for i in range(50):
            skip.insert(i)
            lst.append(i)
        expected = skip.to_list()
        self.assertEqual(lst, expected)  # if failure here, see (4)



    def test_remove(self):

        # (1) delete back on empty list (should do nothing)
        skip = Skip()
        try:
            skip.remove(0)
        except Exception as e:
            self.fail(msg=f"Raised {type(e)} when popping from back of empty list.")

        #remove a node that doesn't exist
        skip = Skip()
        lst = []
        for i in range(5):  # construct list
            skip.insert(i)
            lst.append(i)

        skip.remove(7)
        expected = skip.to_list()
        self.assertEqual(lst, expected)  # if failure here, see (3)

        # (2) pop back on multiple node list
        skip = Skip()
        lst = []
        for i in range(5):          # construct list
            skip.insert(i)
            lst.append(i)
        for i in range(4, 0, -1):          # destruct list
            skip.remove(i)
            lst.pop()
        expected = skip.to_list()
        self.assertEqual(lst, expected)  # if failure here, see (3)

        # (3) remove more, this time from front
        skip = Skip()
        lst = []
        for i in range(50):
            skip.insert(i)
            lst.append(i)
        for i in range(50):
            skip.remove(i)
            lst.pop(0)
        expected = skip.to_list()
        self.assertEqual(lst, expected)  # if failure here, see (3)

    def test_search(self):

        # (1) find in empty skip list
        skip = Skip()
        node = skip.search(331)
        self.assertIsNone(node)

        # (2) find existing value in single-node Skip List
        skip = Skip()
        skip.insert(0)
        node = skip.search(0)
        self.assertIsInstance(node, Node)
        self.assertEqual(0, node.value)

        # (3) find non-existing value in single-node Skip List
        node = skip.search(331)
        self.assertIsNone(node)

        # (4) find in longer Skip List with all unique values
        skip = Skip()
        for i in range(10):
            skip.insert(i)

        node = skip.search(0)
        self.assertIsInstance(node, Node)
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.next[0].value)

        node = skip.search(9)
        self.assertIsInstance(node, Node)
        self.assertIsNone(node.next[0])
        self.assertEqual(9, node.value)

        node = skip.search(4)
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)
        self.assertEqual(5, node.next[0].value)

        node = skip.search(331)
        self.assertIsNone(node)

    def test_application(self):
        #NYC subway system stops according to the MIT lecture
        stops = [14, 23, 34, 42, 50, 59, 66, 72, 79, 86,
                 96, 103, 110, 116, 125]

        random.seed(331)

        skip = Skip()

        for value in stops:
            skip.insert(value)

        # test 1: start or end location doesn't exist
        path = skip.rush(12, 23)
        #start doesn't exist
        self.assertIsNone(path)

        path = skip.rush(14, 331)
        #end doesn't exist
        self.assertIsNone(path)

        # test 2: one stop to the next
        path = skip.rush(14, 23)
        self.assertEqual([14, 23], path)

        # test 3: beginning to middle of route
        path = skip.rush(14, 72)
        self.assertEqual([14, 23, 72], path)

        #test 4: two stops in the middle of the route
        path = skip.rush(34, 110)
        self.assertEqual([34, 42, 50, 59, 66, 72, 103, 110], path)

        #test 5: fastest path beginning to end
        path = skip.rush(14, 125)
        self.assertEqual([14, 23, 103, 110, 125], path)



if __name__ == '__main__':
    unittest.main()
