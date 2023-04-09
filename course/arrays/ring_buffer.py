"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

To run tests: pytest -m arrays
"""


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

    ...
