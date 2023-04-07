"""
To run tests: python -m trees
"""

from typing import List, Optional

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

# Note: for all types of traversal:
# Time: O(n) we need to visit all the nodes anyway
# Space: O(h) recursion depth is equal to a hight of a tree
# where h=n for unbalanced binary tree and h=logn - for a perfectly balanced one.


def pre_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With pre order traversal the output should be: [20, 10, 5,  7, 15, 50, 30, 29, 45, 100]."""

    def walk(current: Optional[BinaryTreeNode], path: List[int]) -> List[int]:
        if not current:
            return path

        # Visit node, recurion, recursion
        path.append(current.value)
        walk(current.left, path)
        walk(current.right, path)
        return path

    return walk(head, [])


def in_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With in order traversal the output should be: [5, 7, 10, 15, 20, 29, 30, 45, 50, 100].

    So use in order traversal if you need to output nodes of a binary search tree in a sorted order.
    For ascending order first visit left node and then right one, for desceding - right node and then left one.
    """

    def walk(current: Optional[BinaryTreeNode], path: List[int]) -> List[int]:
        if not current:
            return path

        # Recursion, visit node, recursion
        walk(current.left, path)
        path.append(current.value)
        walk(current.right, path)
        return path

    return walk(head, [])


def post_order_traversal(head: BinaryTreeNode) -> List[int]:
    """With post order traversal the output should be: [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]."""

    def walk(current: Optional[BinaryTreeNode], path: List[int]) -> List[int]:
        if not current:
            return path

        # Recursion, recurion, visit node
        walk(current.left, path)
        walk(current.right, path)
        path.append(current.value)
        return path

    return walk(head, [])
