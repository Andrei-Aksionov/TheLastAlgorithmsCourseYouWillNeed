import random
from typing import List

import pytest

from course.quick_sort.quick_sort import quick_sort, quick_sort_middle_pivot

# ------------------------------------------------------------------
# ---------------- Quick Sort with pivot in the end ----------------
# ------------------------------------------------------------------


@pytest.mark.quick_sort
def test_quick_sort() -> None:
    # Given
    numbers = [9, 3, 7, 4, 69, 420, 42]
    numbers_sorted = [3, 4, 7, 9, 42, 69, 420]

    # When
    quick_sort(numbers)

    # Then
    assert numbers == numbers_sorted


@pytest.mark.quick_sort
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_quick_sort_auto_tests(numbers: List[int]) -> None:
    # Given
    numbers_sorted = sorted(numbers)

    # When
    quick_sort(numbers)

    # Then
    assert numbers == numbers_sorted


# ---------------------------------------------------------------------
# ---------------- Quick Sort with pivot in the middle ----------------
# ---------------------------------------------------------------------


@pytest.mark.quick_sort
def test_quick_sort_pivot_middle() -> None:
    # Given
    numbers = [9, 3, 7, 4, 69, 420, 42]
    numbers_sorted = [3, 4, 7, 9, 42, 69, 420]

    # When
    quick_sort_middle_pivot(numbers)

    # Then
    assert numbers == numbers_sorted


@pytest.mark.quick_sort
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_quick_sort_auto_tests_middle_pivot(numbers: List[int]) -> None:
    # Given
    numbers_sorted = sorted(numbers)

    # When
    quick_sort_middle_pivot(numbers)

    # Then
    assert numbers == numbers_sorted
