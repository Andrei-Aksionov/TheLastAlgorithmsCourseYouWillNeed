"""
To run tests: python -m maps
"""

from typing import Optional

from course.data_structures import DoublyLinkedNode
from course.maps.dictionary import Dictionary


class LRU:
    """
    Most Recently Used (MRU)                      Least Recently Used (LRU)
      |                                           |
      ⌄                                           ⌄
    -----      -----      -----      -----      -----
    | A | <--> | B | <--> | C | <--> | D | <--> | E |
    -----      -----      -----      -----      -----
      ^                    ^ ^         ^          ^
      |                    | |         |          |
     head               tail |         |         will be dropped with trim_cache()
                             |         |         as it exceeds capacity
                           length   capacity
    """

    # For all operations it's the same time/space complexities
    # Time: O(1) because we do map lookup + linking/unlinking node and it doesn't
    # depend on the size of LRU cache
    # Space: O(1) the sam as for time
    # basically there are no loops or recursions

    def __init__(self, capacity: int = 10) -> None:
        self.length = 0
        self.capacity = capacity
        self.head = self.tail = None
        self.lookup = Dictionary()
        self.reverse_lookup = Dictionary()

    def update(self, key: str, value: int) -> None:
        """Update node's value that is accessed by the key if it exists, create new if doesn't."""

        node = self.lookup.get(key)
        # if node doesn't exist - create one with the value and put it in the beginning
        if node is None:
            node = DoublyLinkedNode(value)
            self._prepend(node)
            # as new node is added in case the length exceeds capacity we need to trim cache
            self._trim_cache()
            self.lookup[key] = node
            self.reverse_lookup[node] = key
        else:
            # if node exists - just put it in the beginning
            self._detach(node)
            self._prepend(node)
            node.value = value

    def get(self, key: int) -> Optional[DoublyLinkedNode]:
        """Return node's value if it can be accessed by the key, in other case - return None."""
        # check cache for existence
        node = self.lookup.get(key)
        if node is None:
            return None

        # update the value we found and move it to the front
        self._detach(node)
        self._prepend(node)

        # return the value we found or None if not exist
        return node.value

    def _detach(self, node: DoublyLinkedNode) -> None:
        # if there is a node in front
        if node.prev:
            node.prev.next = node.next
        # if there is a node behind
        if node.next:
            node.next.prev = node.prev

        # update head/tail if needed
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        # unlink the node
        node.prev = node.next = None

        # don't forget to update the length
        self.length -= 1

    def _prepend(self, node: DoublyLinkedNode) -> None:
        self.length += 1

        # if it's just an empty cache
        if not (self.head and self.tail):
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def _trim_cache(self) -> None:
        """If the length of the cache exceeds it's capacity remove the last node and cleanup lookup tables."""
        if self.length <= self.capacity:
            return

        node = self.tail
        # unlink the last node
        self._detach(node)

        # cleanup lookup tables
        key = self.reverse_lookup.get(node)
        self.lookup.pop(key)
        self.reverse_lookup.pop(node)
