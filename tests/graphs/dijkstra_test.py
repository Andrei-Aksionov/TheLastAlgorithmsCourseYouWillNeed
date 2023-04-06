from typing import List

import pytest

from course.graphs.dijkstra import (
    dijkstra_list_shortest_path,
    dijkstra_list_shortest_path_min_heap,
)
from tests.graphs.graph_examples import graph_list_1, graph_list_2


@pytest.mark.graph
@pytest.mark.parametrize(
    ("graph", "source", "needle", "expected_path"),
    list(
        zip(
            (0, 4, 6, 2, 5),
            (6, 2, 1, 5, 2),
            (graph_list_1, graph_list_1, graph_list_2, graph_list_2, graph_list_2),
            ([0, 1, 4, 5, 6], [4, 1, 2], [], [], [5, 2]),
        ),
    ),
)
def test_dijkstra(graph: List[List[int]], source: int, needle: int, expected_path: List[int]) -> None:
    # When
    path = dijkstra_list_shortest_path(graph, source, needle)

    # Then
    assert path == expected_path


@pytest.mark.graph
@pytest.mark.parametrize(
    ("graph", "source", "needle", "expected_path"),
    list(
        zip(
            (0, 4, 6, 2, 5),
            (6, 2, 1, 5, 2),
            (graph_list_1, graph_list_1, graph_list_2, graph_list_2, graph_list_2),
            ([0, 1, 4, 5, 6], [4, 1, 2], [], [], [5, 2]),
        ),
    ),
)
def test_dijkstra_min_heap(graph: List[List[int]], source: int, needle: int, expected_path: List[int]) -> None:
    # When
    path = dijkstra_list_shortest_path_min_heap(graph, source, needle)

    # Then
    assert path == expected_path
