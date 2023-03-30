import pytest

from course.trees.compare_binary_trees import BinaryNode, compare_bfs, compare_dfs

"""
               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45
"""  # noqa: W605

tree_1 = BinaryNode(
    value=20,
    left=BinaryNode(
        value=10,
        left=BinaryNode(
            value=5,
            right=BinaryNode(
                value=7,
            ),
        ),
        right=BinaryNode(
            value=15,
        ),
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

"""
               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45
                /      \
               21      49
"""  # noqa: W605

tree_2 = BinaryNode(
    value=20,
    left=BinaryNode(
        value=10,
        left=BinaryNode(
            value=5,
            right=BinaryNode(
                value=7,
            ),
        ),
        right=BinaryNode(
            value=15,
        ),
    ),
    right=BinaryNode(
        value=50,
        left=BinaryNode(
            value=30,
            left=BinaryNode(
                value=29,
                left=BinaryNode(
                    value=21,
                ),
            ),
            right=BinaryNode(
                value=45,
                right=BinaryNode(
                    value=49,
                ),
            ),
        ),
    ),
)

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
