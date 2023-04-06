import pytest  # noqa: I001

from course.trees.binary_tree_search import search_bfs, search_dfs
from course.trees.binary_tree_traversal import pre_order_traversal
from tests.trees.tree_examples import tree_1 as tree

#############################################################
################## Breadth First Search #####################
#############################################################


@pytest.mark.binary_tree
@pytest.mark.parametrize(
    ("needle", "expected_result"),
    [(45, True), (7, True), (69, False), (31, False), (15, True), (8, False)],
)
def test_binary_tree_search_bfs(needle: int, expected_result: bool) -> None:
    # When
    result = search_bfs(tree, needle)

    # Then
    assert result == expected_result


@pytest.mark.binary_tree
@pytest.mark.parametrize(
    "needle",
    pre_order_traversal(tree),
)
def test_binary_tree_search_bfs_auto(needle: int) -> None:
    # When
    result = search_bfs(tree, needle)

    # Then
    assert result is True


#############################################################
################### Depth First Search ######################
#############################################################


@pytest.mark.binary_tree
@pytest.mark.parametrize(
    ("needle", "expected_result"),
    [(45, True), (7, True), (69, False), (31, False), (15, True), (8, False)],
)
def test_binary_tree_search_dfs(needle: int, expected_result: bool) -> None:
    # When
    result = search_dfs(tree, needle)

    # Then
    assert result == expected_result


@pytest.mark.binary_tree
@pytest.mark.parametrize(
    "needle",
    pre_order_traversal(tree),
)
def test_binary_tree_search_dfs_auto(needle: int) -> None:
    # When
    result = search_dfs(tree, needle)

    # Then
    assert result is True
