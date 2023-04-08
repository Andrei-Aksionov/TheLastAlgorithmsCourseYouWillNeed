"""
To run tests: pytest -m sort
"""

from typing import Optional

from course.data_structures import StackLinkedNode


class Stack:
    """
    -----    -----    -----    -----
    | A | <- | B | <- | C | <- | D |
    -----    -----    -----    -----
                                 ↑
                                head
    """

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, number: int) -> None:
        """Push element to the end of the stack."""

        # Time: O(1) no matter what the size of the linked list adding new node
        #   to the end is always constant
        # Space: O(1) each time we just need to allocate a space for a single node
        #   no matter what's the size of the linked list

        node = StackLinkedNode(number)
        self.length += 1

        # if it's an empty stack
        if self.head:
            node.prev = self.head
        self.head = node

    def pop(self) -> Optional[int]:
        """Pop element from the end of the stack (the last added element)."""

        # Time: O(1) no matter what the size of the linked list unlinkage of the last
        #   node is always constant
        # Space: O(1) no new memory is created

        # if it's an empty stack
        if not self.head:
            return None

        self.length -= 1

        old_head = self.head
        self.head = self.head.prev
        # unlink old head
        old_head.prev = None
        return old_head.value

    def peek(self) -> Optional[int]:
        """Show value of the element at the end of the stack without modifying the stack."""

        # Time: O(1) accessing value by link
        # Space: O(1) no new space is created

        return self.head.value if self.head else None
