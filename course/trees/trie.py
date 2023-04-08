"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

To run tests: pytest -m trees
"""

from typing import List

from course.data_structures import TrieNode


class Trie:
    """

    Note: there are only three branches at max for each node simply because it's easier to draw :)
    Each node can have [0, +inf] children.

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

    def __init__(self) -> None:
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        """Insert new word in the trie tree."""

        # Time: O(n) because we need to iterate over all chars of the inputted word
        # Space: O(n) at worst we need to create TrieNodes and insert for all the chars
        # n - length of the word to insert

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
        node.is_word_end = True

    def find(self, prefix: str) -> List[str]:
        """Find all branches for the provided prefix.

        If the tree contains ["foo", "fool", "foolish", "bar"] and the prefix is "foo"
        the output will be ["foo", "fool", "foolish"]
        """

        # Time: O(n + nr) we need to iterate over the whole prefix + traverse all
        # remaining nodes
        # Space: O(h - n) stack will store the whole branch minus prefix
        # n - total number of nodes of the trie, h - height of the trie,
        # nr - remaining nodes

        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        def traverse(node: TrieNode, prefix: str, words: List[str]) -> None:
            """Depth-first traversal of the trie."""
            if node.is_word_end:
                words.append(prefix + node.char)

            for child in node.children.values():
                traverse(child, prefix + node.char, words)

        words = []
        traverse(node, prefix[:-1], words)

        return words

    def delete(self, prefix: str) -> None:
        """Deletes the prefix from the trie.

        This one is a bit trickier: if the last character doesn't have children we need to delete
        all characters up until the next .is_word_end char.

        For example the trie contains: ["fo", "foo", "fool", "foolish"]
        If we want to delete `foolish` we can simply mark `h` as .is_word_end=False, so it will not be returned with
        `find` method, but it still will be in the memory. So we can delete nodes up until character `l` because
        it's the end of the longest word with the same prefix as our target.
        At the same time if we want to delete `foo` we just need to mark `o` as not the end character, otherwise
        we will loose ["fool", "foolish"]
        """

        # Time: O(n) we need to iterate over the whole prefix
        # Space: O(n) stack will store the same number of nodes as chars in the prefix
        # n - length of the prefix

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
        node.is_word_end = False

        # if there other nodes after the current one - simply quit
        if len(node.children) > 1:
            return

        # if after the last character there is nothing we can remove every char
        # until next is_word_end=True
        while stack:
            node = stack.pop()
            if node.is_word_end or len(node.children) > 1:
                break
            node.children = {}
