from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    prev: Optional["Node"] = None
    next: Optional["Node"] = None  # noqa: A003


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head: Node = None
        self.tail: Node = None

    def get(self, idx: int) -> int:
        """Get a node's value at provided index."""
        if idx > self.length:
            raise ValueError(f"You are trying to get at idx={idx}, but the number of node is {self.length}t")
        return self._get_node(idx).value

    def prepend(self, item: int) -> None:
        """Add item to the beginning of the linked list.

        ← B ⇿ C →  ==>  ← A ⇿ B ⇿ C →
        """
        node = Node(item)
        self.length += 1
        # if it's an empty linked list
        if not (self.head and self.tail):
            self.head = self.tail = node
            return
        # update links so the new node is in the beginning of the linked list
        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, item: int) -> None:
        """Add item to the end of the linked list.

        ← A ⇿ B →  ==>  ← A ⇿ B ⇿ C →
        """
        node = Node(item)
        self.length += 1
        # if it's an empty linked list
        if not (self.head and self.tail):
            self.head = self.tail = node
            return
        # update links so the new node is in the end of the linked list
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def insert_at(self, item: int, idx: int) -> None:
        """Insert item at the arbitrary position that's specified by idx value.

        ← A ⇿ B →  ==>  ← A    B →
                           ⤡  ⤢
                            C
        """
        if idx > self.length:
            raise ValueError(f"You are trying to insert at idx={idx}, but the number of node is {self.length}")
        if idx == 0:
            self.prepend(item)
            return
        if idx == self.length:
            self.append(item)
            return

        current = self._get_node(idx)

        node = Node(item)
        self.length += 1
        node.prev = current.prev
        node.next = current
        current.prev = node
        if node.prev:
            node.prev.next = node

    def remove_at(self, idx: int) -> int:
        """Remove item at the arbitrary position that's specified by idx value.

        ← A ⇿ B ⇿ C →  ==>  ← A ⇿ C →
        """
        if idx > self.length:
            raise ValueError(f"You are trying to insert at idx={idx}, but the number of node is {self.length}")

        node = self._traverse_linked_list(idx)

        return self._remove_node(node)

    def remove(self, item: int) -> Optional[int]:
        """Remove node with the same value as provided item."""
        node = self.head
        while node and node.value != item:
            node = node.next

        # if node is None that means that we traversed over the whole linked list
        # and haven't found a node with the same value as item
        if not node:
            return None

        return self._remove_node(node)

    def _traverse_linked_list(self, idx: int) -> Node:
        # if index is equal to the beginning or the end of the linked list
        # it means that there is no need to traverse, just return head or tail correspondingly
        if idx == 0:
            return self.head
        if idx == self.length:
            return self.tail
        # if the index is in the first half of the linked list - start from the beginning
        # if not - from the end
        first_half = idx <= self.length // 2
        node = self.head if first_half else self.tail
        idx = idx if first_half else self.length - idx - 1

        iteration = 0
        while node and iteration < idx:
            node = node.next if first_half else node.prev
            iteration += 1

        return node

    def _get_node(self, idx: int) -> Node:
        """Helper function: get node of the linked list at index."""
        return self._traverse_linked_list(idx)

    def _remove_node(self, node: Node) -> int:
        """Helper function: delete provided node and reassign `prev` and `next` links.

        ← A ⇿ B ⇿ C →  ==>  ← A ⇿ C →
        """
        # if we need to delete the last remaining node
        if self.length == 1:
            self.length -= 1
            node.next = node.prev = None
            self.head = self.tail = None
            return node.value

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # if deleted node was head or tail don't forget to update them
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        # unlink deleted node
        node.prev = node.next = None
        self.length -= 1

        return node.value
