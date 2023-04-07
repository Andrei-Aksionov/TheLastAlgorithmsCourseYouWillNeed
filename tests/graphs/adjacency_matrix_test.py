from typing import List

import pytest

from course.graphs.adjacency_matrix import adjacency_list_dfs, adjacency_matrix_bfs
from course.utils import is_empty_function
from tests.graphs.graph_examples import (
    graph_list_1,
    graph_list_2,
    graph_matrix_1,
    graph_matrix_2,
)


@pytest.mark.graph
class TestAdjacencyMatrixAndList:
    ########################################################
    ################# Graph as a Matrix ####################
    ########################################################

    @pytest.mark.skipif(is_empty_function(adjacency_matrix_bfs), reason="non implemented function adjacency_matrix_bfs")
    @pytest.mark.parametrize(
        ("graph", "source", "needle", "expected_path"),
        list(
            zip(
                (graph_matrix_1, graph_matrix_2, graph_matrix_1, graph_matrix_2),
                (0, 0, 1, 6),
                (2, 6, 0, 0),
                ([0, 3, 2], [0, 1, 4, 5, 6], None, None),
            ),
        ),
    )
    def test_adjacency_matrix_bfs(
        self,
        graph: List[List[int]],
        source: int,
        needle: int,
        expected_path: List[int],
    ) -> None:
        # When
        path = adjacency_matrix_bfs(graph, source, needle)

        # Then
        assert path == expected_path

    ########################################################
    ################## Graph as a List #####################
    ########################################################

    @pytest.mark.skipif(is_empty_function(adjacency_list_dfs), reason="non implemented function adjacency_list_dfs")
    @pytest.mark.parametrize(
        ("graph", "source", "needle", "expected_path"),
        list(
            zip(
                (graph_list_1, graph_list_1, graph_list_2, graph_list_2),
                (0, 5, 0, 6),
                (5, 3, 6, 0),
                ([0, 1, 2, 3, 4, 5], [5, 2, 0, 1, 4, 3], [0, 1, 4, 5, 6], None),
            ),
        ),
    )
    def test_adjacency_list_dfs(
        self,
        graph: List[List[int]],
        source: int,
        needle: int,
        expected_path: List[int],
    ) -> None:
        # When
        path = adjacency_list_dfs(graph, source, needle)

        # Then
        assert path == expected_path
