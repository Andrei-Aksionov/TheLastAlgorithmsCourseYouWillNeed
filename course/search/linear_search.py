"""
To run tests: python -m search
"""

from typing import List


def linear_search(haystack: List[int], needle: int) -> bool:
    # O(n) time | O(1) space
    for item in haystack:
        if item == needle:
            return True
    return False
