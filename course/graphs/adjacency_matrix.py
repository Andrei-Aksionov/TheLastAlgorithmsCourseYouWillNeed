"""
          Graph                        Adjacency Matrix

           (10)                         0   1   2   3
      [0] ➜  ➜  ➜ [1]                 ----|---|---|---|
       ↑  ⬊  (5)   ↑                0 |  0  10   0   5
   (7) ↑     ⬊     ↑ (1)            1 |  0   0   0   0
       ↑   (2)   ⬊ ↑                2 |  7   0   0   0
      [2] ←  ←  ← [3]               3 |  0   1   2   0

    Legend: [] - node
            () - weight
            ➜  - direction

To run tests: python -m graphs
"""

from collections import deque
from typing import List, Optional

from course.data_structures import GraphEdge


def adjacency_matrix_bfs(graph: List[List[int]], source: int, needle: int) -> Optional[List[int]]:
    # Time: O(n^2) because we need to visit every adjacent node of each node
    # Space: O(n^2) we need to store for each node adjacency to other nodes

    # For better understanding let's use the graph depicted above
    # Assume that our starting point (source) is 10 and our needle is 2

    # we need to track nodes that were already visited
    # and how we got to the node (from what node)
    seen = [False] * len(graph)
    previous = [-1] * len(graph)

    seen[source] = True
    queue = deque([source])

    while queue:
        # First iter: current = 0
        #   Second iter: current = 1
        #       Third iter: current = 3
        #           Fourth iter: current = 2 --> break 'cause we found the needle
        current = queue.popleft()
        if current == needle:
            break

        # First iter: adjacencies = [0, 10, 0, 5]
        #   Second iter: adjacencies = [0, 0, 0, 0]
        #       Third iter: adjacencies = [0, 1, 2, 0]
        adjacencies = graph[current]
        for idx in range(len(adjacencies)):
            # if it's 0 - there is no connection to a node with value of idx
            if adjacencies[idx] == 0:
                continue
            # if already visited this node
            if seen[idx]:
                continue
            seen[idx] = True
            previous[idx] = current
            queue.append(idx)
        # First iter: - seen = [False, True, False, True]
        #           | - previous = [-1, 0, -1, 0]
        #           | - queue = [1, 3]
        #   Second iter: the same as above except queue:
        #              | - queue = [3]
        #       Third iter: - seen = [False, True, True, True]
        #                 | - previous = [-1, 0, 3, 0]
        #                 | - queue = [2]

    # basically if haven't visited the node
    # perhaps because of lacking connection between source and needle
    if previous[needle] == -1:
        return None

    # build it backwards: from needle to source
    current = needle
    out = []

    # First iter: current = 3
    #           | out = [2]
    #   Second iter: current = 0
    #              | out = [2, 3]
    while previous[current] != -1:
        out.append(current)
        current = previous[current]

    # The final result is [0, 3, 2]
    return [source] + out[::-1]


def adjacency_list_dfs(graph: List[GraphEdge], source: int, needle: int) -> Optional[List[int]]:
    # V - vertex/node, E - edge (connection between nodes)
    # Time: O(V + E) because we need to visit all nodes by all connections
    # Space: O(V + E) the same as for time complexity

    def walk(graph: List[GraphEdge], current: int, needle: int, seen: List[bool], path: List[int]) -> bool:
        if seen[current]:
            return False
        seen[current] = True

        # Recurse step
        # pre
        path.append(current)
        if current == needle:
            return True
        # recursion
        adjacencies: List[GraphEdge] = graph[current]
        for edge in adjacencies:
            if walk(graph, edge.to, needle, seen, path):
                return True

        # post
        # clean `path` if we haven't found the needle
        path.pop()

        return False

    seen = [False] * len(graph)
    path = []
    walk(graph, source, needle, seen, path)
    return path or None
