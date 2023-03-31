from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryTreeNode:
    value: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None
