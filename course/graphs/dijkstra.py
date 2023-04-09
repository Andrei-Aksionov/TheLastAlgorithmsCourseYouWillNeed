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

    Video explanation: https://youtu.be/pVfj6mxhdMw

    Example task: find the shortest path from 0 to 1
    Possible paths: 0 -> 1 (weight of 10), 0 -> 3 -> 1 (weight 6)

    On each iteration find the shortest path from the current node to an unseen reachable (distance not infinity) node.
        On iteration 1 it will be {
            0: 0,
            1: 10,
            3: 5,
        }
        an write down how to we get here {
            0: 0,
            1: 0,
            3: 0,
        }
    Out of all nodes for which distance was updated find an unseen node with the smallest distance;
    on the first iteration it will be 3

    Repeat the above until we mark all reachable nodes as seen or until we find our needle/sink
        On iteration 2 distances are {
            0: 0,
            1: 6,
            3: 5,
        }
        how to we get here {
            0: 0,
            1: 3,
            3: 0,
        }

    On the next iteration we will visit node 1 (our needle/sink) so we can stop.

    Iterate over the list of nodes from which we came from and return this path.
    For this examples the answer is: [0, 3, 1]

To run tests: pytest -m graphs
"""

from typing import List

from course.data_structures import GraphEdge


def dijkstra_list_shortest_path(source: int, sink: int, arr: List[GraphEdge]) -> List[int]:
    ...


def dijkstra_list_shortest_path_min_heap(source: int, sink: int, arr: List[GraphEdge]) -> List[int]:
    # Note: this one is an optional: was explained in the video but the implementation wasn't shown.
    # But it's good for better understanding of algorithms and MinHeap to try to implement it.
    # Stuck? Take a look at the 'answers' branch.
    ...
