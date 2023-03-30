from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryNode:
    value: int
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None


def compare_bfs(a: BinaryNode, b: BinaryNode) -> bool:
    # Time: O(hn) because we need to compare at worst n/2+1 elements at h levels
    # Note: n/2+1 for perfectly balanced binary tree and 1 - for extremely unbalanced
    # Space: O(n) because at worst we need to store n/2+1 elements (for each tree)
    def fill_level(queue: deque) -> deque:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        return queue

    queue_a = deque([a])
    queue_b = deque([b])

    while queue_a and queue_b:
        # compare shape
        if len(queue_a) != len(queue_b):
            return False
        # compare values
        for node_a, node_b in zip(queue_a, queue_b):
            if node_a.value != node_b.value:
                return False

        fill_level(queue_a)
        fill_level(queue_b)

    # either both are empty or only one is empty
    return len(queue_a) == len(queue_b)


def compare_dfs(a: Optional[BinaryNode], b: Optional[BinaryNode]) -> bool:
    # Time: O(n) because we need to traverse all nodes at worst
    # Space: O(h) because we traverse as many steps as deep is the tree
    # Note: n - number of elements of the smallest tree, h - height of the smallest tree

    # compare shape/structure
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    # compare values
    if a.value != b.value:
        return False

    return compare_dfs(a.left, b.left) and compare_dfs(a.right, b.right)
