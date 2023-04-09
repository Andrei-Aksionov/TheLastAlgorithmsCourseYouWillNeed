import pytest

from course.trees.binary_tree_traversal import (
    in_order_traversal,
    post_order_traversal,
    pre_order_traversal,
)
from course.utils import is_empty_function
from tests.trees.tree_examples import tree_1 as tree


@pytest.mark.trees
class TestBinaryTreeTraversal:
    @pytest.mark.skipif(is_empty_function(pre_order_traversal), reason="non implemented function pre_order_traversal")
    def test_binary_tree_pre_order_traversal(self) -> None:
        # Given
        expected_path = [20, 10, 5, 7, 15, 50, 30, 29, 45, 100]

        # When
        path = pre_order_traversal(tree)

        # Then
        assert path == expected_path

    @pytest.mark.skipif(is_empty_function(in_order_traversal), reason="non implemented function in_order_traversal")
    def test_binary_tree_in_order_traversal(self) -> None:
        # Given
        expected_path = [5, 7, 10, 15, 20, 29, 30, 45, 50, 100]

        # When
        path = in_order_traversal(tree)

        # Then
        assert path == expected_path

    @pytest.mark.skipif(is_empty_function(post_order_traversal), reason="non implemented function post_order_traversal")
    def test_binary_tree_post_order_traversal(self) -> None:
        # Given
        expected_path = [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]

        # When
        path = post_order_traversal(tree)

        # Then
        assert path == expected_path
