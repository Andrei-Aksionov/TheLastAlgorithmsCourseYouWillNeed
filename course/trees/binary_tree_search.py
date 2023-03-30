from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryNode:
    value: int
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None


def search_dfs(head: Optional[BinaryNode], needle: int) -> bool:
    if head is None:
        return False
    if head.value == needle:
        return True

    if needle <= head.value:
        return search_dfs(head.left, needle)
    return search_dfs(head.right, needle)
