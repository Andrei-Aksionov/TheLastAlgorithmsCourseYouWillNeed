from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BinaryNode:
    value: int
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None


def walk(current: Optional[BinaryNode], path: List[int]) -> List[int]:
    if not current:
        return path

    # Recurions

    # pre
    path.append(current.value)

    # recurse
    walk(current.left, path)
    walk(current.right, path)

    # post
    return path


def pre_order_search(head: BinaryNode) -> List[int]:
    return walk(head, [])
