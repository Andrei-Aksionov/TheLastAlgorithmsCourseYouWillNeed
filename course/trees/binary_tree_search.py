"""

       Binary Search Tree

               20
              /  \
         10          50
        /  \        /  \
       5    15     30   100
        \         /  \
         7       29   45


To run tests: pytest -m trees
"""

from typing import Optional

from course.data_structures import BinaryTreeNode


def search_dfs(head: Optional[BinaryTreeNode], needle: int) -> bool:
    ...


def search_bfs(head: BinaryTreeNode, needle: int) -> bool:
    ...
