from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    prev: Optional["Node"] = None


class Stack:
    # -----    -----    -----    -----
    # | A | <- | B | <- | C | <- | D |
    # -----    -----    -----    -----
    #                              ↑
    #                             head
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, number: int) -> None:
        """Push element to the end of the stack."""
        node = Node(number)
        self.length += 1

        # if it's an empty stack
        if not self.head:
            self.head = node
        else:
            node.prev = self.head
            self.head = node

    def pop(self) -> Optional[int]:
        """Pop element from the end of the stack (the last added element)."""
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
        return self.head.value if self.head else None
