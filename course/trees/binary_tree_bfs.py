from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryNode:
    value: int
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None


def breadth_first_search(head: BinaryNode, needle: int) -> bool:
    # Time: O(n^2) if to use regular list, O(n) - with deque structure
    # Space: O(n), more specifically O(1) in a extremely unbalanced tree,
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
