"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

To run tests: pytest -m trees
"""


class Trie:
    """

    Note: there are only three branches at max for each node simply because it's easier to draw :)
    Each node can have [0, +inf] children.

                Root
                / \
               b   f
              /     \
             a      [o]
            /        /\
          [z]      [o] u
                   /    \
                 [l]     n
                 /        \
                i          d - r - [y]
               /          / \
              s          e   a
             /          /     \
           [h]        [r]      t
                                \
                                 i
                                  \
                                   o
                                    \
                                    [n]

    Legeng: [x] - end of the word
    """

    ...
