import random

import pytest

from course.search.two_crystal_balls import two_crystal_balls, two_crystal_balls_logn

# ----------------------- sqrt(n) solution -----------------------


@pytest.mark.search
@pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
def test_two_crystal_balls(size: int) -> None:
    # Given
    idx = random.randint(0, size - 1)
    data = [False] * idx + [True] * (size - idx)

    # When
    result = two_crystal_balls(data)

    # Then
    assert result == idx


@pytest.mark.search
@pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
def test_two_crystal_balls_not_found(size: int) -> None:
    # Given
    data = [False] * size

    # When
    result = two_crystal_balls(data)

    # Then
    assert result == -1


# ----------------------- log(n) solution -----------------------


@pytest.mark.search
@pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
def test_two_crystal_balls_logn(size: int) -> None:
    # Given
    idx = random.randint(0, size - 1)
    data = [False] * idx + [True] * (size - idx)

    # When
    result = two_crystal_balls_logn(data)

    # Then
    assert result == idx


@pytest.mark.search
@pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
def test_two_crystal_balls_logn_not_found(size: int) -> None:
    # Given
    data = [False] * size

    # When
    result = two_crystal_balls_logn(data)

    # Then
    assert result == -1
