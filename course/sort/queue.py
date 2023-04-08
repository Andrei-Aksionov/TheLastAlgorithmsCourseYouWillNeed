"""
To run tests: pytest -m sort
"""

from typing import Optional

from course.data_structures import SinglyLinkedNode


class Queue:
    """
    -----    -----    -----    -----
    | A | -> | B | -> | C | -> | D |
    -----    -----    -----    -----
      ↑                          ↑
    head                        tail
    """

    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, value: int) -> None:
        """Add element to the end of the queue."""

        # Time: O(1) no matter what the size of the linked list adding new node
        #   to the end is always constant
        # Space: O(1) each time we just need to allocate a space for a single node
        #   no matter what's the size of the linked list

        node = SinglyLinkedNode(value)
        self.length += 1

        # if it's an empty queue
        if not (self.head and self.tail):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Optional[int]:
        """Pop the first element of the queue."""

        # Time: O(1) no matter what the size of the linked list unlinkage of the first
        #   node is always constant
        # Space: O(1) no new memory is created

        # if it's an empty queue
        if not self.head:
            return None

        self.length -= 1

        old_head = self.head
        self.head = self.head.next

        # unlink old head
        old_head.next = None
        # if it's an empty queue also update tail
        if not self.length:
            self.tail = None

        return old_head.value

    def peek(self) -> Optional[int]:
        """Show what value will be dequeued without changing queue."""

        # Time: O(1) accessing value by link
        # Space: O(1) no new space is created

        return self.head.value if self.head else None
