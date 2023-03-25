from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    # O(n^2) time | O(1) space

    # each time one largest value will be moved to the right
    for i in range(len(arr)):
        # -1 because we check `j + 1`
        # -i: each time we move the largest values to the right and no need to process them,
        # so check values until that are already moved
        for j in range(len(arr) - 1 - i):
            # larger value should be moved to the right
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
