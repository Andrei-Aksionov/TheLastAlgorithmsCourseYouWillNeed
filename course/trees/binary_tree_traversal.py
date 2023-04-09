"""
To run tests: pytest -m trees
"""

from typing import List

from course.data_structures import BinaryTreeNode

"""
Let's use this tree as an example input for the algorithms below.

               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45
"""


def pre_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With pre order traversal the output should be: [20, 10, 5,  7, 15, 50, 30, 29, 45, 100]."""

    ...


def in_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With in order traversal the output should be: [5, 7, 10, 15, 20, 29, 30, 45, 50, 100].

    So use in order traversal if you need to output nodes of a binary search tree in a sorted order.
    For ascending order first visit left node and then right one, for desceding - right node and then left one.
    """

    ...


def post_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With post order traversal the output should be: [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]."""

    ...
