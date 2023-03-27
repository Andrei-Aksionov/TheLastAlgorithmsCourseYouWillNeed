from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


def walk(
    maze: List[List[str]],
    wall: str,
    current: Point,
    end: Point,
    seen: List[List[bool]],
    path: List[Point],
) -> bool:
    # --- Base case ---
    # off the map
    if any((current.x < 0, current.x >= len(maze[0]), current.y < 0, current.y >= len(maze))):
        return False
    # on the wall
    if maze[current.y][current.x] == wall:
        return False
    # if already seen the point
    if seen[current.y][current.x]:
        return False
    # at the end
    if current == end:
        # do not forget to add the final point to the path
        path.append(current)
        return True

    # --- Recursion ---
    seen[current.y][current.x] = True
    # pre
    path.append(current)

    # recursion
    for shift_x, shift_y in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # up -> right -> down -> left
        new_current = Point(current.x + shift_x, current.y + shift_y)
        if walk(maze, wall, new_current, end, seen, path):
            return True

    # post
    # pop if the path led to a dead end
    path.pop()

    return False


def maze_solver(maze: List[List[str]], wall: str, start: Point, end: Point) -> List[Point]:
    seen = [[False] * len(maze[0]) for _ in range(len(maze))]
    path = []

    walk(maze, wall, start, end, seen, path)

    return path


def draw_path(maze: List[List[str]], path: List[Point]) -> List[str]:
    maze = [list(row) for row in maze]

    for point in path:
        if maze[point.y][point.x] != " ":
            raise ValueError(f"It's not an empty point in the maze: {point}")
        maze[point.y][point.x] = "*"

    print("\n".join(["".join(row) for row in maze]))  # noqa: T201


if __name__ == "__main__":
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
        # end
    ]
    result = maze_solver(maze=maze, wall="x", start=Point(10, 0), end=Point(1, 5))
    draw_path(maze, result)
