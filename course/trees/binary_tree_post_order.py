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

    # recurse
    walk(current.left, path)
    walk(current.right, path)

    # post
    path.append(current.value)
    return path


def post_order_search(head: BinaryNode) -> List[int]:
    return walk(head, [])
