# TODO: remake it as a adjacency list
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
    Out of all nodes for which distance was updated find unseen node with the smallest distance;
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

"""

from dataclasses import dataclass
from typing import List


@dataclass
class GraphEdge:
    to: int
    weight: int


def get_lowest_unvisited(seen: List[bool], distances: List[int]) -> int:
    """Return an index of the node with the lowest distance."""

    lowest_distance_idx = -1
    lowest_distance = float("inf")

    for idx in range(len(seen)):
        if seen[idx]:
            continue

        if distances[idx] < lowest_distance:
            lowest_distance = distances[idx]
            lowest_distance_idx = idx

    return lowest_distance_idx


def dijkstra_list_shortest_path(source: int, sink: int, arr: List[GraphEdge]) -> List[int]:
    # V - number of nodes (vertexes), E - number of connection (edges)
    # Time: O(V^2 + E) because we need to find for each node the node with the lowest distance,
    # which in intself iterates over all nodes and then for each node we need to check it's edges,
    # which means that in the end we will check all the edges
    # Space: O(V) because we need to store seen, previous and distances arrays that have the size of V

    seen = [False] * len(arr)  # what nodes we already visited
    previous = [-1] * len(arr)  # how did we get to the node
    distances = [float("inf")] * len(arr)  # the shortest path to the node
    distances[source] = 0

    while True:
        current = get_lowest_unvisited(seen, distances)
        # if there is no unseen node with the distance smaller than infinity
        if current == -1:
            break
        # if we have already found the needle/sink
        if current == sink:
            break
        # don't forted to mark the node as visited
        seen[current] = True

        # iterate over all connected nodes to the current one
        for edge in arr[current]:
            if seen[edge.to]:
                continue

            # update distance for each node that can be reached
            distance = distances[current] + edge.weight
            if distance < distances[edge.to]:
                distances[edge.to] = distance
                previous[edge.to] = current

    # if we haven't found a path
    if previous[sink] == -1:
        return []

    # write down the path from needle/sink to the source
    out = []
    current = sink

    while previous[current] != -1:
        out.append(current)
        current = previous[current]

    out.append(source)
    return out[::-1]


def dijkstra_list_shortest_path_min_heap(source: int, sink: int, arr: List[GraphEdge]) -> List[int]:  # noqa: ARG001
    # TODO: implement dijkstra algorithm with min heap
    # that will reduce time complexity from O(V^2 + E) ---> O(logV*(V+E))
    # because we need to iterate over all nodes by all edges anyway, but everytime
    # we need the smallest distance we need to update min heap, which has time complexity of O(logn), where
    # n in our case is V (the number of nodes)
    ...
