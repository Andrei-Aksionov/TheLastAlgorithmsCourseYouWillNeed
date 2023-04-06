import pytest

from course.trees.trie import Trie


@pytest.mark.trie
def test_trie() -> None:
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


@pytest.mark.trie
def test_not_found_prefix_return_empty_list() -> None:
    # Given
    trie = Trie()

    # Then
    assert trie.find("foo") == []


@pytest.mark.trie
def test_not_found_prefix_to_delete_return_none() -> None:
    # Given
    trie = Trie()

    # Then
    assert trie.delete("foo") is None
