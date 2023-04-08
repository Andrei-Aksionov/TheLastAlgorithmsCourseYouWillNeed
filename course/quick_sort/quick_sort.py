"""
To run tests: pytest -m quick_sort
"""

from typing import List

# ------------------------------------------------------------------
# ---------------- Quick Sort with pivot in the end ----------------
# ------------------------------------------------------------------


def quick_sort(numbers: List[int]) -> List[int]:
    # Time: O(nlogn) sorting n elements logn times
    # Space: O(nlogn) because stack will stores all elements on logn level,
    # but since it's done inplace, no extra space is used so as a result O(1) space

    def partition(numbers: List[int], low: int, high: int) -> int:
        # input: -> [9, 8, 1, 3, 5] <-
        # step 1: use the last number as a pivot
        #   [9, 8, 1, 3 , |5|] use `5` as pivot
        # step 2: move all numbers that are smaller or equal to pivot to the begginning
        #   [1, 3, 9, 8, |5|]
        # step 3: move pivot number to the place after the last replacement
        # -> [1, 3, 5, 9, 8] <-

        pivot = numbers[high]

        # there are two pointer: slow and fast
        # fast is updated more frequently and is looking for a value that is smaller
        # or equal than the pivot number,
        # slow is updated only after we did a replacement
        slow = low

        for fast in range(low, high):
            if numbers[fast] <= pivot:
                numbers[slow], numbers[fast] = numbers[fast], numbers[slow]
                slow += 1

        numbers[high] = numbers[slow]
        numbers[slow] = pivot

        return slow

    def quick_sort_recursive(numbers: List[int], low: int, high: int) -> None:
        if low >= high:
            return

        pivot_idx = partition(numbers, low, high)
        quick_sort_recursive(numbers, low, pivot_idx - 1)
        quick_sort_recursive(numbers, pivot_idx + 1, high)

    quick_sort_recursive(numbers, 0, len(numbers) - 1)


# ---------------------------------------------------------------------
# ---------------- Quick Sort with pivot in the middle ----------------
# ---------------------------------------------------------------------


def quick_sort_middle_pivot(numbers: List[int]) -> List[int]:
    # Time: O(nlogn) sorting n elements logn times
    # Space: O(nlogn) because stack will stores all elements on logn level,
    # but since it's done inplace, no extra space is used so as a result O(1) space

    def quick_sort_recursive(numbers: List[int], left: int, right: int) -> List[int]:
        i, j = left, right
        # in this implementation pivot is the middle number
        pivot = numbers[(i + j) // 2]

        while i <= j:
            # look for a number that is larger then the pivot number
            while numbers[i] < pivot:
                i += 1
            # look for a number that is smaller then the pivot number
            while numbers[j] > pivot:
                j -= 1
            if i <= j:
                # after swapping all the numbers that are smaller then the pivot number
                # will be at it's left, all the larger numbers - at it's right
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i, j = i + 1, j - 1

        # if j is greater than left boundary then not all numbers that are smaller
        # than the pivot are moved to the left
        if j > left:
            quick_sort_recursive(numbers, left, j)
        # the same here, but not all numbers that are bigger than the pivot
        if i < right:
            quick_sort_recursive(numbers, i, right)

    return quick_sort_recursive(numbers, 0, len(numbers) - 1)
