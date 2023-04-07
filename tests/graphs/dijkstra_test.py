from typing import List

import pytest

from course.graphs.dijkstra import (
    dijkstra_list_shortest_path,
    dijkstra_list_shortest_path_min_heap,
)
from course.utils import is_empty_function
from tests.graphs.graph_examples import graph_list_1, graph_list_2


@pytest.mark.graphs
class TestDijkstra:
    @pytest.mark.skipif(
        is_empty_function(dijkstra_list_shortest_path),
        reason="non implemented function dijkstra_list_shortest_path",
    )
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
    def test_dijkstra(
        self,
        graph: List[List[int]],
        source: int,
        needle: int,
        expected_path: List[int],
    ) -> None:
        # When
        path = dijkstra_list_shortest_path(graph, source, needle)

        # Then
        assert path == expected_path

    @pytest.mark.skipif(
        is_empty_function(dijkstra_list_shortest_path_min_heap),
        reason="non implemented function dijkstra_list_shortest_path_min_heap",
    )
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
    def test_dijkstra_min_heap(
        self,
        graph: List[List[int]],
        source: int,
        needle: int,
        expected_path: List[int],
    ) -> None:
        # When
        path = dijkstra_list_shortest_path_min_heap(graph, source, needle)

        # Then
        assert path == expected_path
