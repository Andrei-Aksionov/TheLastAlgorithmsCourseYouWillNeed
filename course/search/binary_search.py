"""
To run tests: pytest -m search
"""

from typing import List

"""
This implementation reflects of what was shown in the video, only in Python.
I personally not a huge fun of it, that's why it's commented out

def binary_search(haystack: List[int], needle: int) -> bool:
    lo = 0
    hi = len(haystack)

    while lo < hi:
        m = math.floor(lo + (hi - lo) / 2)
        v = haystack[m]
        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1
    return False
"""


def binary_search(haystack: List[int], needle: int) -> bool:
    # Time: O(logn) each time we split haystack by a factor of 2
    # Space: O(1) no extra storage is used

    left = 0
    right = len(haystack) - 1

    while left <= right:
        middle = (left + right) // 2
        if needle < haystack[middle]:
            right = middle - 1
        elif needle > haystack[middle]:
            left = middle + 1
        else:
            return True
    return False
