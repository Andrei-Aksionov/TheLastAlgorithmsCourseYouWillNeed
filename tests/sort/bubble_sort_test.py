import random
from typing import List

import pytest

from course.sort.bubble_sort import bubble_sort


@pytest.mark.sort
def test_bubble_sort() -> None:
    # Given
    arr_unsorted = [9, 3, 7, 4, 69, 420, 42]
    arr_sorted = [3, 4, 7, 9, 42, 69, 420]

    # When
    result = bubble_sort(arr_unsorted)

    # Then
    assert result == arr_sorted


@pytest.mark.sort
@pytest.mark.parametrize("arr", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_bubble_sort_auto_tests(arr: List[int]) -> None:
    # Given
    arr_sorted = sorted(arr)

    # When
    result = bubble_sort(arr)

    # Then
    assert result == arr_sorted
