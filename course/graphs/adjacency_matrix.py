"""
          Graph                        Adjacency Matrix         Adjacency List

           (10)                         0   1   2   3
      [0] ➜  ➜  ➜ [1]                 ----|---|---|---|         {
       ↑  ⬊  (5)   ↑                0 |  0  10   0   5            0: [{"to": 1, "weight": 10}, {"to": 3, "weight": 5}],
   (7) ↑     ⬊     ↑ (1)            1 |  0   0   0   0            1: [],
       ↑   (2)   ⬊ ↑                2 |  7   0   0   0            2: [{"to": 0, "weight": 7}],
      [2] ←  ←  ← [3]               3 |  0   1   2   0            3: [{"to": 1, "weight": 1}, {"to": 2, "weight": 2}],
                                                                }

    Legend: [] - node
            () - weight
            ➜  - direction

To run tests: pytest -m graphs
"""

from typing import List, Optional

from course.data_structures import GraphEdge


def adjacency_matrix_bfs(graph: List[List[int]], source: int, needle: int) -> Optional[List[int]]:
    ...


def adjacency_list_dfs(graph: List[GraphEdge], source: int, needle: int) -> Optional[List[int]]:
    ...
