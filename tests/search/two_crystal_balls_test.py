import random

import pytest

from course.search.two_crystal_balls import two_crystal_balls, two_crystal_balls_logn
from course.utils import is_empty_function


@pytest.mark.search
class TestTwoCrystalBalls:
    # ----------------------------------------------------------------
    # ----------------------- sqrt(n) solution -----------------------
    # ----------------------------------------------------------------

    @pytest.mark.skipif(is_empty_function(two_crystal_balls), reason="non implemented function two_crystal_balls")
    @pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
    def test_two_crystal_balls(self, size: int) -> None:
        # Given
        idx = random.randint(0, size - 1)
        data = [False] * idx + [True] * (size - idx)

        # When
        result = two_crystal_balls(data)

        # Then
        assert result == idx

    @pytest.mark.skipif(is_empty_function(two_crystal_balls), reason="non implemented function two_crystal_balls")
    @pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
    def test_two_crystal_balls_not_found(self, size: int) -> None:
        # Given
        data = [False] * size

        # When
        result = two_crystal_balls(data)

        # Then
        assert result == -1

    # ----------------------------------------------------------------
    # ------------------------ log(n) solution -----------------------
    # ----------------------------------------------------------------

    @pytest.mark.skipif(
        is_empty_function(two_crystal_balls_logn),
        reason="non implemented function two_crystal_balls_logn",
    )
    @pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
    def test_two_crystal_balls_logn(self, size: int) -> None:
        # Given
        idx = random.randint(0, size - 1)
        data = [False] * idx + [True] * (size - idx)

        # When
        result = two_crystal_balls_logn(data)

        # Then
        assert result == idx

    @pytest.mark.skipif(
        is_empty_function(two_crystal_balls_logn),
        reason="non implemented function two_crystal_balls_logn",
    )
    @pytest.mark.parametrize("size", [1, 100, 10000, *random.sample(range(1, 10000), 10)])
    def test_two_crystal_balls_logn_not_found(self, size: int) -> None:
        # Given
        data = [False] * size

        # When
        result = two_crystal_balls_logn(data)

        # Then
        assert result == -1
