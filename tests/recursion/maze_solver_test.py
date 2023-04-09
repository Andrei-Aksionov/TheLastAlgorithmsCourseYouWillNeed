import pytest

from course.data_structures import Point
from course.recursion.maze_solver import maze_solver
from course.utils import is_empty_function


@pytest.mark.recursion
@pytest.mark.skipif(is_empty_function(maze_solver), reason="non implemented function maze_solver")
class TestMazeSolver:
    def test_maze_solver(self) -> None:
        # Given
        # starting from top to end end
        maze = [
            #        start
            #          ↓
            "xxxxxxxxxx x",
            "x        x x",
            "x        x x",
            "x xxxxxxxx x",
            "x          x",
            "x xxxxxxxxxx",
            # ↑
            # end
        ]

        expected_maze_result = [
            Point(x=10, y=0),
            Point(x=10, y=1),
            Point(x=10, y=2),
            Point(x=10, y=3),
            Point(x=10, y=4),
            Point(x=9, y=4),
            Point(x=8, y=4),
            Point(x=7, y=4),
            Point(x=6, y=4),
            Point(x=5, y=4),
            Point(x=4, y=4),
            Point(x=3, y=4),
            Point(x=2, y=4),
            Point(x=1, y=4),
            Point(x=1, y=5),
        ]
        # When
        result = maze_solver(maze=maze, wall="x", start=Point(10, 0), end=Point(1, 5))

        # Then
        assert result == expected_maze_result

    def test_maze_solver_dead_end(self) -> None:
        """The difference between this test and the one above is that it has false path
        that opens at (7, 3) and leads to a dead end. Maze solver should remove this path
        from the final output."""
        # Given
        # starting from top to end end
        maze = [
            #        start
            #          ↓
            "xxxxxxxxxx x",
            "x        x x",
            "x        x x",
            "xxxxxxx xx x",
            "x          x",
            "x xxxxxxxxxx",
            # ↑
            # no end
        ]

        expected_maze_result = [
            Point(x=10, y=0),
            Point(x=10, y=1),
            Point(x=10, y=2),
            Point(x=10, y=3),
            Point(x=10, y=4),
            Point(x=9, y=4),
            Point(x=8, y=4),
            Point(x=7, y=4),
            Point(x=6, y=4),
            Point(x=5, y=4),
            Point(x=4, y=4),
            Point(x=3, y=4),
            Point(x=2, y=4),
            Point(x=1, y=4),
            Point(x=1, y=5),
        ]
        # When
        result = maze_solver(maze=maze, wall="x", start=Point(10, 0), end=Point(1, 5))

        # Then
        assert result == expected_maze_result
