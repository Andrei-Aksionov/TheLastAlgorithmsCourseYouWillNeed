"""

       Binary Search Tree

               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45


To run tests: pytest -m trees
"""

from collections import deque
from typing import Optional

from course.data_structures import BinaryTreeNode


def search_binary_search_tree(head: Optional[BinaryTreeNode], needle: int) -> bool:
    """Just an example of how it can be easier to find a node in a binary search tree."""

    # Note: it's not covered by tests as it's just for an example

    # Time: O(n) at worst we need to iterate over all nodes
    # Space: O(1) no extra space is used

    node = head
    while node:
        if needle < node.value:
            node = node.left
        elif needle > node.value:
            node = node.right
        else:
            return node
    return None


def search_dfs(head: Optional[BinaryTreeNode], needle: int) -> bool:
    # Time: O(n) in the worst case we need to check all nodes
    # Space: O(h) in the worst case recursion depth is the height of a tree
    # h=n if binary tree is extremely unbalanced, h=logn - perfectly balanced

    if head is None:
        return False
    if head.value == needle:
        return True

    if needle <= head.value:
        return search_dfs(head.left, needle)
    return search_dfs(head.right, needle)


def search_bfs(head: BinaryTreeNode, needle: int) -> bool:
    # Time: O(n^2) if to use regular list, O(n) - with deque structure,
    # where n is the total number of nodes
    # Space: O(h), more specifically O(1) in an extremely unbalanced tree,
    # O(n/2+1) with perfectly balanced binary tree

    # Note: this implementation of BFS will work on any binary tree, not only on binary search tree.

    queue: deque = deque([head])

    while queue:
        node = queue.popleft()
        if not node:
            continue

        if node.value == needle:
            return True

        queue.append(node.left)
        queue.append(node.right)

    return False
