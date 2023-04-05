"""
Note: there are only two branches at max for each node simply because it's easier to draw :)
Each node can have [0, +inf] nodes.

            Root
            / \
           b   f
          /     \
         a      [o]
        /        /\
      [z]      [o] u
               /    \
             [l]     n
             /        \
            i          d - r - [y]
           /          / \
          s          e   a
         /          /     \
       [h]        [r]      t
                            \
                             i
                              \
                               o
                                \
                                [n]

Legeng: [x] - end of the word

"""
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class TrieNode:
    char: str
    # if this node is an end char of the word
    is_end: bool = False
    # every node has from 0 to inf children
    children: Dict[str, "TrieNode"] = field(default_factory=dict)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        """Insert new word in the trie tree."""

        # Time: O(h) because at worst we need to traverse the whole branch
        # Space: O(h) at worst we need to insert all the chars
        # h - height of the trie

        # start from the root of the trie
        node = self.root

        # iterate over all characters of the word
        for char in word:
            # if the node has a child with the same value as char
            if char in node.children:
                node = node.children[char]
            # if there is no child with the same value as char
            # create new node and attach it to other children of the node
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # node with the final char should be marked so it's clear that this is the full word
        node.is_end = True

    def find(self, prefix: str) -> List[str]:
        """Find all branches for the provided prefix.

        If the tree contains ["foo", "fool", "foolish", "bar"] and the prefix is "foo"
        the output will be ["foo", "fool", "foolish"]
        """

        # Time: O(n) at worst we need to return all children of the root recursively
        # Space: O(h) stack will store the whole branch
        # n - total number of nodes of the trie, h - height of the trie

        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        def traverse(node: TrieNode, prefix: str, words: List[str]) -> None:
            """Depth-first traversal of the trie."""
            if node.is_end:
                words.append(prefix + node.char)

            for child in node.children.values():
                traverse(child, prefix + node.char, words)

        words = []
        traverse(node, prefix[:-1], words)

        return words

    def delete(self, prefix: str) -> None:
        """Deletes the prefix from the trie.

        This one is a bit trickier: if the last character doesn't have children we need to delete
        all characters up until the next .is_end char.

        For example the trie contains: ["fo", "foo", "fool", "foolish"]
        If we want to delete `foolish` we can simply mark `h` as .is_end=False, so it will not be returned with
        `find` method, but it still will be in the memory. So we can delete nodes up until character `l` because
        it's the end of the longest word with the same prefix as our target.
        At the same time if we want to delete `foo` we just need to mark `o` as not the end character, otherwise
        we will loose ["fool", "foolish"]
        """

        # Time: O(h) at worst we need to delete the whole branch of the trie
        # Space: O(h) at worst the stack will store the whole branch
        # h - height of the trie

        node = self.root
        # stack contains branch of the trie for the prefix
        stack = [node]

        for char in prefix:
            if char not in node.children:
                return
            node = node.children[char]
            stack.append(node)

        # mark the last char as not the end in any case
        node = stack.pop()
        node.is_end = False

        # if there other nodes after the current one - simply quit
        if len(node.children) > 1:
            return

        # if after the last character there is nothing we can remove every char
        # until next is_end=True
        while stack:
            node = stack.pop()
            if node.is_end or len(node.children) > 1:
                break
            node.children = {}
