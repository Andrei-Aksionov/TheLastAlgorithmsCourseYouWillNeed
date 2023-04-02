from typing import List

import pytest

from course.graphs.adjacency_matrix import adjacency_matrix_bfs
from tests.graphs.graph_examples import graph_1, graph_2


@pytest.mark.graph
@pytest.mark.parametrize(
    ("graph", "source", "needle", "expected_path"),
    list(
        zip(
            (graph_1, graph_2),
            (0, 0),
            (2, 6),
            ([0, 3, 2], [0, 1, 4, 5, 6]),
        ),
    ),
)
def test_adjacency_matrix_bfs(graph: List[List[int]], source: int, needle: int, expected_path: List[int]) -> None:
    # When
    path = adjacency_matrix_bfs(graph, source, needle)

    # Then
    assert path == expected_path


@pytest.mark.graph
@pytest.mark.parametrize(
    ("graph", "source", "needle", "expected_path"),
    list(
        zip(
            (graph_1, graph_2),
            (1, 6),
            (0, 0),
            (None, None),
        ),
    ),
)
def test_adjacency_matrix_bfs_return_none(
    graph: List[List[int]],
    source: int,
    needle: int,
    expected_path: List[int],
) -> None:
    # When
    path = adjacency_matrix_bfs(graph, source, needle)

    # Then
    assert path == expected_path
