import pytest

from course.trees.compare_binary_trees import compare_bfs, compare_dfs
from tests.trees.tree_examples import tree_1, tree_2

#############################################################
################# Breadth First Search ######################
#############################################################


@pytest.mark.binary_tree
def test_compare_binary_tree_breadth_first_similar() -> None:
    # Given
    tree_a = tree_1
    tree_b = tree_1

    # When
    result = compare_bfs(tree_a, tree_b)

    # Then
    assert result is True


@pytest.mark.binary_tree
def test_compare_binary_tree_breadth_first_different() -> None:
    # Given
    tree_a = tree_1
    tree_b = tree_2

    # When
    result = compare_bfs(tree_a, tree_b)

    # Then
    assert result is False


#############################################################
################# Depth First Search ########################
#############################################################


@pytest.mark.binary_tree
def test_compare_binary_tree_depth_first_similar() -> None:
    # Given
    tree_a = tree_1
    tree_b = tree_1

    # When
    result = compare_dfs(tree_a, tree_b)

    # Then
    assert result is True


@pytest.mark.binary_tree
def test_compare_binary_tree_depth_first_different() -> None:
    # Given
    tree_a = tree_1
    tree_b = tree_2

    # When
    result = compare_dfs(tree_a, tree_b)

    # Then
    assert result is False
