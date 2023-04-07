import pytest

from course.trees.binary_tree_search import search_bfs, search_dfs
from course.trees.binary_tree_traversal import pre_order_traversal
from course.utils import is_empty_function
from tests.trees.tree_examples import tree_1 as tree


@pytest.mark.binary_tree
class TestBinaryTreeSearch:
    #############################################################
    ################## Breadth First Search #####################
    #############################################################

    @pytest.mark.skipif(is_empty_function(search_bfs), reason="non implemented function search_bfs")
    @pytest.mark.parametrize(
        ("needle", "expected_result"),
        [(45, True), (7, True), (69, False), (31, False), (15, True), (8, False)],
    )
    def test_binary_tree_search_bfs(self, needle: int, expected_result: bool) -> None:
        # When
        result = search_bfs(tree, needle)

        # Then
        assert result == expected_result

    @pytest.mark.skipif(is_empty_function(search_bfs), reason="non implemented function search_bfs")
    @pytest.mark.parametrize(
        "needle",
        pre_order_traversal(tree),
    )
    def test_binary_tree_search_bfs_auto(self, needle: int) -> None:
        # When
        result = search_bfs(tree, needle)

        # Then
        assert result is True

    #############################################################
    ################### Depth First Search ######################
    #############################################################

    @pytest.mark.skipif(is_empty_function(search_dfs), reason="non implemented function search_dfs")
    @pytest.mark.parametrize(
        ("needle", "expected_result"),
        [(45, True), (7, True), (69, False), (31, False), (15, True), (8, False)],
    )
    def test_binary_tree_search_dfs(self, needle: int, expected_result: bool) -> None:
        # When
        result = search_dfs(tree, needle)

        # Then
        assert result == expected_result

    @pytest.mark.skipif(is_empty_function(search_dfs), reason="non implemented function search_dfs")
    @pytest.mark.parametrize(
        "needle",
        pre_order_traversal(tree),
    )
    def test_binary_tree_search_dfs_auto(self, needle: int) -> None:
        # When
        result = search_dfs(tree, needle)

        # Then
        assert result is True
