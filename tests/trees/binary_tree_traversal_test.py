import pytest

from course.trees.binary_tree_in_order import BinaryNode, in_order_search
from course.trees.binary_tree_post_order import post_order_search
from course.trees.binary_tree_pre_order import pre_order_search

"""
export const tree: BinaryNode<number> = {
    value: 20,
    right: {
        value: 50,
        right: {
            value: 100,
            right: null,
            left: null,
        },
        left: {
            value: 30,
            right: {
                value: 45,
                right: null,
                left: null,
            },
            left: {
                value: 29,
                right: null,
                left: null,
            }
        },
    },
    left: {
        value: 10,
        right: {
            value: 15,
            right: null,
            left: null,
        },
        left: {
            value: 5,
            right: {
                value: 7,
                right: null,
                left: null,
            },
            left: null,
        }
    }
};
"""

tree = BinaryNode(
    value=20,
    left=BinaryNode(
        value=10,
        left=BinaryNode(
            value=5,
            right=BinaryNode(value=7),
        ),
        right=BinaryNode(value=15),
    ),
    right=BinaryNode(
        value=50,
        left=BinaryNode(
            value=30,
            left=BinaryNode(
                value=29,
            ),
            right=BinaryNode(
                value=45,
            ),
        ),
        right=BinaryNode(
            value=100,
        ),
    ),
)


@pytest.mark.binary_tree
def test_pre_order_binary_tree_traversal() -> None:
    # Given
    expected_path = [20, 10, 5, 7, 15, 50, 30, 29, 45, 100]

    # When
    path = pre_order_search(tree)

    # Then
    assert path == expected_path


@pytest.mark.binary_tree
def test_in_order_binary_tree_traversal() -> None:
    # Given
    expected_path = [5, 7, 10, 15, 20, 29, 30, 45, 50, 100]

    # When
    path = in_order_search(tree)

    # Then
    assert path == expected_path


@pytest.mark.binary_tree
def test_post_order_binary_tree_traversal() -> None:
    # Given
    expected_path = [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]

    # When
    path = post_order_search(tree)

    # Then
    assert path == expected_path
