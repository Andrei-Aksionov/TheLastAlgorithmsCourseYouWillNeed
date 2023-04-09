import pytest

from course.trees.trie import Trie
from course.utils import is_empty_class


@pytest.mark.trees
@pytest.mark.skipif(is_empty_class(Trie), reason="non implemented class Trie")
class TestTrie:
    def test_trie(self) -> None:
        # This one is taken (and adopted for python) from the ThePrimeagen repo:
        # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/Trie.ts
        # that was used for testing in the video course

        trie = Trie()
        trie.insert("fo")
        trie.insert("foo")
        trie.insert("fool")
        trie.insert("foolish")
        trie.insert("foundation")
        trie.insert("bar")

        assert sorted(trie.find("fo")) == ["fo", "foo", "fool", "foolish", "foundation"]

        # delete the shortest word
        trie.delete("fo")
        assert sorted(trie.find("fo")) == ["foo", "fool", "foolish", "foundation"]

        # delete the longest word
        trie.delete("foundation")
        assert sorted(trie.find("fo")) == ["foo", "fool", "foolish"]

        # delete the middle word
        trie.delete("fool")
        assert sorted(trie.find("fo")) == ["foo", "foolish"]

        # check that another branch is not affected
        assert trie.find("b") == ["bar"]

    def test_not_found_prefix_return_empty_list(self) -> None:
        # Given
        trie = Trie()

        # Then
        assert trie.find("foo") == []

    def test_not_found_prefix_to_delete_return_none(self) -> None:
        # Given
        trie = Trie()

        # Then
        assert trie.delete("foo") is None
