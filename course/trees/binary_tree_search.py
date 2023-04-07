from collections import deque
from typing import Optional

from course.data_structures import BinaryTreeNode


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
    # Space: O(h), more specifically O(1) in a extremely unbalanced tree,
    # O(n/2 + 1) with perfectly balanced binary tree

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
