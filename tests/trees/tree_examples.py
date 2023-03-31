from course.trees.binary_tree_node import BinaryTreeNode

"""
Trees side-by-side

             Tree 1                              Tree 2

               20                                  20
              /  \                                /  \
         10          50                      10          50
        /  \        /  \                    /  \        /  \
       5    15     30   100                5    15     30   100
        \         /  \                      \         /  \
         7       29   45                     7       29   45
                                                    /      \
                                                   21      49
"""  # noqa: W605

# ----------------------------------------------------------------------

"""
             Tree 1

               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45
"""  # noqa: W605

tree_1 = BinaryTreeNode(
    value=20,
    left=BinaryTreeNode(
        value=10,
        left=BinaryTreeNode(
            value=5,
            right=BinaryTreeNode(
                value=7,
            ),
        ),
        right=BinaryTreeNode(
            value=15,
        ),
    ),
    right=BinaryTreeNode(
        value=50,
        left=BinaryTreeNode(
            value=30,
            left=BinaryTreeNode(
                value=29,
            ),
            right=BinaryTreeNode(
                value=45,
            ),
        ),
        right=BinaryTreeNode(
            value=100,
        ),
    ),
)

"""
             Tree 2

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

tree_2 = BinaryTreeNode(
    value=20,
    left=BinaryTreeNode(
        value=10,
        left=BinaryTreeNode(
            value=5,
            right=BinaryTreeNode(
                value=7,
            ),
        ),
        right=BinaryTreeNode(
            value=15,
        ),
    ),
    right=BinaryTreeNode(
        value=50,
        left=BinaryTreeNode(
            value=30,
            left=BinaryTreeNode(
                value=29,
                left=BinaryTreeNode(
                    value=21,
                ),
            ),
            right=BinaryTreeNode(
                value=45,
                right=BinaryTreeNode(
                    value=49,
                ),
            ),
        ),
    ),
)
