"""
To run tests: pytest -m search
"""

from typing import List


def linear_search(haystack: List[int], needle: int) -> bool:
    # Time: O(n) we need to traverse over all elements ones at worst case
    # Space: O(1) no extra storage is used
    for item in haystack:
        if item == needle:
            return True
    return False
