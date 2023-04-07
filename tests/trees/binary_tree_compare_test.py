import pytest

from course.trees.compare_binary_trees import compare_bfs, compare_dfs
from course.utils import is_empty_function
from tests.trees.tree_examples import tree_1, tree_2


@pytest.mark.binary_tree
class TestBinaryTreeComparison:
    #############################################################
    ################## Breadth First Search #####################
    #############################################################

    @pytest.mark.skipif(is_empty_function(compare_bfs), reason="non implemented function compare_bfs")
    def test_compare_binary_tree_breadth_first_similar(self) -> None:
        # Given
        tree_a = tree_1
        tree_b = tree_1

        # When
        result = compare_bfs(tree_a, tree_b)

        # Then
        assert result is True

    @pytest.mark.skipif(is_empty_function(compare_bfs), reason="non implemented function compare_bfs")
    def test_compare_binary_tree_breadth_first_different(self) -> None:
        # Given
        tree_a = tree_1
        tree_b = tree_2

        # When
        result = compare_bfs(tree_a, tree_b)

        # Then
        assert result is False

    #############################################################
    ################### Depth First Search ######################
    #############################################################

    @pytest.mark.skipif(is_empty_function(compare_dfs), reason="non implemented function compare_dfs")
    def test_compare_binary_tree_depth_first_similar(self) -> None:
        # Given
        tree_a = tree_1
        tree_b = tree_1

        # When
        result = compare_dfs(tree_a, tree_b)

        # Then
        assert result is True

    @pytest.mark.skipif(is_empty_function(compare_dfs), reason="non implemented function compare_dfs")
    def test_compare_binary_tree_depth_first_different(self) -> None:
        # Given
        tree_a = tree_1
        tree_b = tree_2

        # When
        result = compare_dfs(tree_a, tree_b)

        # Then
        assert result is False
