"""
Note: it's an optional algorithm that was explained in the course, but not implemented.
"""

from typing import Optional


class RingBuffer:
    """
    -----------------------------
    |   1  |   2  |   3  |   4  |
    -----------------------------
        ↑                    ↑
       head                tail

    after adding 5 and 6:

    -----------------------------
    |   5  |   6  |   3  |   4  |
    -----------------------------
               ↑      ↑
             tail    head

    Capacity is 4 elements. When `5` was added it was placed at the place of `1`,
    the next value of 6 is placed after `5` (where `2` was previously).
    When `.pop` method is called it should return value where the tail is,
        `get` should apply offset from the head
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.head = 0
        self.tail = -1

    def get(self, idx: int) -> Optional[int]:
        if idx >= self.capacity:
            raise ValueError(f"idx should not be larger or equal to capacity of {self.capacity}")
        if idx < 0:
            raise ValueError("Negative indices are not supported.")
        # need to adjust to the nature of ring buffer
        idx = (self.head + idx) % self.capacity
        return self.data[idx]

    def push(self, value: int) -> None:
        self.tail += 1
        if self.tail >= self.capacity:
            self.head += 1
        self.data[self.tail % self.capacity] = value

    def pop(self) -> Optional[int]:
        if self.tail < 0:
            return None

        value = self.data[self.tail % self.capacity]
        # it's not necessary to set None instead of pushed value, but it helps
        # for debugging (makes `data` less cluttered)
        self.data[self.tail % self.capacity] = None
        self.tail -= 1
        self.head = max(0, self.head - 1)
        return value
