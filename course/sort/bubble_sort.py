"""
To run tests: pytest -m sort
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    # Time: O(n^2) as for each element we need to traverse n times
    # Space: O(1) as no extra space is used, all is done inplace

    # each time one largest value will be moved to the right
    for i in range(len(arr)):
        # -1 because we check `j + 1`
        # -i: each time we move the largest values to the right and no need to process them,
        #   so check values until that are already moved
        for j in range(len(arr) - 1 - i):
            # larger value should be moved to the right
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
