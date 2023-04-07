"""
This file contains data structures that are used among algorithms.
"""

from typing import Dict, Optional

################################################################
######################### Linked List ##########################
################################################################


class StackLinkedNode:
    def __init__(
        self,
        value: int,
        prev: Optional["StackLinkedNode"] = None,
    ) -> None:
        self.value = value
        self.prev = prev


class SinglyLinkedNode:
    def __init__(
        self,
        value: int,
        next: Optional["SinglyLinkedNode"] = None,  # noqa: A002
    ) -> None:
        self.value = value
        self.next = next

    def __hash__(self) -> int:
        return hash(self.value)


class DoublyLinkedNode(SinglyLinkedNode):
    def __init__(
        self,
        value: int,
        prev: Optional["DoublyLinkedNode"] = None,
        next: Optional["DoublyLinkedNode"] = None,  # noqa: A002
    ) -> None:
        super().__init__(value, next)
        self.prev = prev


################################################################
############################ Tree ##############################
################################################################


class BinaryTreeNode:
    def __init__(
        self,
        value: int,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self, char: str, children: Dict[str, "TrieNode"] = None, is_word_end: bool = False) -> None:
        self.char = char
        # every node has from 0 to inf children
        self.children = children or {}
        # if this node is an end char of the word
        self.is_word_end = is_word_end


################################################################
############################ Graph #############################
################################################################


class GraphEdge:
    def __init__(self, to: int, weight: int) -> None:
        self.to = to
        self.weight = weight


################################################################
######################### Maze solver ##########################
################################################################


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y
