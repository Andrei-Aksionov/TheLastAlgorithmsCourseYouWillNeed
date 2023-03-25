from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None  # noqa: A003


class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, value: int) -> None:
        """Add element to the end of the queue."""
        new_node = Node(value)
        self.length += 1

        # if it's an empty queue
        if not (self.head and self.tail):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> int:
        """Pop the first element of the queue."""
        # if it's an empty queue
        if not self.head:
            raise ValueError("You are trying to dequeue an empty queue")

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
        return self.head.value if self.head else None
