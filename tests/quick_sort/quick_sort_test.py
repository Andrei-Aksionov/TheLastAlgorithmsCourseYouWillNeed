import random
from typing import List

import pytest

from course.quick_sort.quick_sort import quick_sort, quick_sort_middle_pivot
from course.utils import is_empty_function


@pytest.mark.quick_sort
class TestQuickSort:
    # ------------------------------------------------------------------
    # ---------------- Quick Sort with pivot in the end ----------------
    # ------------------------------------------------------------------

    @pytest.mark.skipif(is_empty_function(quick_sort), reason="non implemented function quick_sort")
    def test_quick_sort(self) -> None:
        # Given
        numbers = [9, 3, 7, 4, 69, 420, 42]
        numbers_sorted = [3, 4, 7, 9, 42, 69, 420]

        # When
        quick_sort(numbers)

        # Then
        assert numbers == numbers_sorted

    @pytest.mark.skipif(is_empty_function(quick_sort), reason="non implemented function quick_sort")
    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_quick_sort_auto_tests(self, numbers: List[int]) -> None:
        # Given
        numbers_sorted = sorted(numbers)

        # When
        quick_sort(numbers)

        # Then
        assert numbers == numbers_sorted

    # ---------------------------------------------------------------------
    # ---------------- Quick Sort with pivot in the middle ----------------
    # ---------------------------------------------------------------------

    @pytest.mark.skipif(
        is_empty_function(quick_sort_middle_pivot),
        reason="non implemented function quick_sort_middle_pivot",
    )
    def test_quick_sort_pivot_middle(self) -> None:
        # Given
        numbers = [9, 3, 7, 4, 69, 420, 42]
        numbers_sorted = [3, 4, 7, 9, 42, 69, 420]

        # When
        quick_sort_middle_pivot(numbers)

        # Then
        assert numbers == numbers_sorted

    @pytest.mark.skipif(
        is_empty_function(quick_sort_middle_pivot),
        reason="non implemented function quick_sort_middle_pivot",
    )
    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_quick_sort_auto_tests_middle_pivot(self, numbers: List[int]) -> None:
        # Given
        numbers_sorted = sorted(numbers)

        # When
        quick_sort_middle_pivot(numbers)

        # Then
        assert numbers == numbers_sorted
