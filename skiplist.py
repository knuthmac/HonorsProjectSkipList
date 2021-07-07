"""
Honors Project
CSE 331 S21 (Onsay)
Macinze Knuth
skiplist.py
"""

from typing import TypeVar
import random

T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)


class Node:
    """
    Implementation of a skip list node.
    """
    __slots__ = ["value", "next"]

    def __init__(self, value=None, next=None) -> None:
        """
        Construct a skip list node.
        :param value: value held by the Node.
        :param next: reference to the next List of Nodes in the skip list.
        :return: None.
        """
        self.value = value
        if next is None:
            next = [None]      #Node of height 3 will have three next pointers for each level
        self.next = next

        # a node is the list of towers, think of like vertical lists

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return str(self.value)

    def __str__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return str(self.value)


class Skip:
    """
    Implementation of a skip list.
    """
    __slots__ = ["head", "max_height"]

    def __init__(self) -> None:
        """
        Construct an empty skip linked list.
        :return: None.
        """
        self.head = Node()
        self.max_height = 1

    def update(self, current, val, update=None) -> Node:
        '''
        description: traverse through the skip list while keeping track of the levels to find the
        value searched for
        best case run time complexity: O(log n) because it cuts through each layer
        worse case: O(n) if it has to search each node in the bottom layer
        :param current: the current node being looked at
        :param key: the value to search for
        :param update: if inserting or removing a node, will keep track of the previous levels
        :return: the Node before the node searched for
        '''

        for level in range(self.max_height-1, -1, -1):
            while current.next[level] and current.next[level].value < val:
                current = current.next[level]
            if update is not None:
                update[level] = current
        return current

    def search(self, val) -> Node:
        '''
        description: traverses through the list to find a value
        best case run time complexity: O(log n) because it cuts through each layer
        worse case: O(n) if it has to search each node in the bottom layer
        :param val: the value to search for
        :return: the node if found, otherwise none
        '''

        if self.head.next[0] is None:
            return None

        current = self.head

        # find the node before the insert
        current = self.update(current, val, update=None)

        found = current.next[0]

        if found is None:
            return None
        elif found.value == val:
            return found
        else:
            return None


    def flip_coin(self) -> bool:
        '''
        description: flips the coin to randomly determine if the height of the skip list should
        increase
        :return: bool, true if the height should increase, false otherwise
        '''
        return random.choice([True, False])

    def random_height(self) -> int:
        '''
        description: determines the height of the node by randomly flipping a coin
        :return: height
        '''
        height = 1
        while self.flip_coin():
            height += 1
        return height

    def insert(self, val) -> None:
        '''
        description: inserts the value into the skip list
        best case run time complexity: O(log n) because it cuts through each layer
        worse case: O(n) if it has to search each node in the bottom layer
        :param val: the Node's value
        :return: None
        '''

        current = self.head
        before = [None] * self.max_height

        #find the node to the left of insert
        #use before to make an updated copy of the skip list
        current = self.update(current, val, before)

        if current.next[0] and current.next[0].value == val:
            # if the value is already there, do nothing
            return None
        else:
            height = self.random_height()

            new_next = []

            for level, node in enumerate(before[:height]):
                new_next.append(node.next[level])

            if height > self.max_height:
                #update the difference if the height is higher

                diff = height - self.max_height
                new_next += [None] * diff
                self.head.next += [None] * diff
                before += [self.head] * diff
                self.max_height = height

            new_node = Node(value=val, next=new_next)

            #update the previous nodes to point at the new node
            for level, node in enumerate(before[:height]):
                node.next[level] = new_node


    def remove(self, val) -> None:
        '''
        description: removes a node from the skip list
        best case run time complexity: O(log n) because it cuts through each layer
        worse case: O(n) if it has to search each node in the bottom layer
        :param val: the val Node to remove
        :return: None
        '''

        if self.head.next[0] is None:
            return None

        current = self.head
        before = [None] * self.max_height

        current = self.update(current, val, before)

        del_node = current.next[0]

        # if the node doens't exist, do nothing
        if del_node is None:
            return None

        if del_node and del_node.value == val:
            for level, forward in enumerate(del_node.next):
                before[level].next[level] = forward
        else:
            return None


    def to_list(self):
        '''
        description: turns the bottom lane into a list for testing purposes, making sure the
        value was inserted or removed properly
        run time complexity: O(n)
        :return: list of all the skip list values
        '''
        level = 0
        result = []
        current = self.head
        while current.next[level] and current.next[level].value is not None:
            result.append(current.next[level].value)
            current = current.next[level]

        return result


    def rush(self, start, end):
        '''
        description: you're in a rush, find the quickest NYC route between two locations!
        best case run time complexity: O(log n) because it cuts through each layer
        worse case: O(n) if it has to search each node in the bottom layer
        :param start: the start location
        :param end: the end location
        :return: list of the quickest path between two locations
        '''

        is_start = self.search(start)
        is_end = self.search(end)
        if is_end is None or is_start is None:
            return None

        result = []
        result.append(start)
        current = is_start

        level = len(current.next) - 1
        while level > -1:
            while current.next[level] and current.next[level].value <= end:
                result.append(current.next[level].value)
                current = current.next[level]
                level = len(current.next) - 1
            level -= 1

        return result
