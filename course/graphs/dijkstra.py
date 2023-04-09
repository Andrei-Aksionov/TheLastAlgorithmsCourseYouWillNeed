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

import heapq
from typing import List

from course.data_structures import GraphEdge


def get_lowest_unvisited(seen: List[bool], distances: List[int]) -> int:
    """Return an index of the node with the lowest distance."""

    # Time: O(V) as we need to check all nodes of the graph
    # Space: O(1) no external storage is used

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


def dijkstra_list_shortest_path_min_heap(source: int, sink: int, arr: List[GraphEdge]) -> List[int]:
    # Note: this is an optional algorithm; it was explained in the video but not implemented

    # dijkstra algorithm with min heap
    # that will reduce time complexity from O(V^2 + E) ---> O(logV*(V+E))
    # because we need to iterate over all nodes by all edges anyway, but everytime
    # we need the smallest distance we need to update min heap, which has time complexity of O(logn), where
    # n in our case is V (the number of nodes)

    seen = [False] * len(arr)  # what nodes we already visited
    previous = [-1] * len(arr)  # how did we get to the node
    distances = [float("inf")] * len(arr)  # the shortest path to the node
    distances[source] = 0
    current_distances = [(0, source)]  # here we will store distances to an unseen nodes

    while current_distances:
        # previously in order to find an unvisited node with the smallest distance
        # we had to traverse over all nodes O(n)
        # now with help of MinHeap we can do it in O(1) because the smallest distance
        # node is in the top of MinHeap
        # with combination of pushing to MinHeap it reduces overall time complexity from O(n) -> O(logn)
        current_distance, current_node = heapq.heappop(current_distances)
        # if we have already found the needle/sink
        if current_node == sink:
            break
        # don't forted to mark the node as visited
        seen[current_node] = True

        # iterate over all connected nodes to the current one
        for edge in arr[current_node]:
            if seen[edge.to]:
                continue

            # update distance for each node that can be reached
            distance = current_distance + edge.weight
            if distance < distances[edge.to]:
                distances[edge.to] = distance
                previous[edge.to] = current_node
                # pushing to MinHeap is O(logn) time complexity
                heapq.heappush(current_distances, (distance, edge.to))

    # if we haven't found a path
    if previous[sink] == -1:
        return []

    # write down the path from needle/sink to the source
    out = []
    current_node = sink

    while previous[current_node] != -1:
        out.append(current_node)
        current_node = previous[current_node]

    out.append(source)
    return out[::-1]
