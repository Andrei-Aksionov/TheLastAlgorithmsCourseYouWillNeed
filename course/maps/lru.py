"""
To run tests: pytest -m maps
"""


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

    ...
