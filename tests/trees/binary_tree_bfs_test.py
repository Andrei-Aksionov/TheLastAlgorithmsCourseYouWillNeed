import pytest

from course.trees.binary_tree_bfs import BinaryNode, breadth_first_search

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
@pytest.mark.parametrize(("needle", "expected_result"), [(45, True), (7, True), (69, False)])
def test_pre_order_binary_tree_traversal(needle: int, expected_result: bool) -> None:
    # When
    result = breadth_first_search(tree, needle)

    # Then
    assert result == expected_result
