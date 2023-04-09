"""
To run tests: pytest -m heap
"""


class MinHeap:
    """
                               Min Heap

                  Values                           Indices

                    50                                0
                 /      \                           /    \
              71          100                     1        2
            /    \        /  \                  /  \      /  \
          101    80     200   105              3    4    5    6
          /                                   /
         106                                 7

    Indices: [0,  1,  2,   3,   4,  5,   6,   7  ]
    Values:  [50, 71, 100, 101, 80, 200, 105, 106]

          parent
            |
        [(i-1)/2]
            |
          _____
          | i |
          -----
        /       \
      2i+1     2i+2
      /           \
    left          right
    child         child

    """

    ...
