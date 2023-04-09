"""
To run tests: pytest -m search
"""

from typing import List


def two_crystal_balls(breaks: List[bool]) -> int:
    ...


# it is possible to solve that exact problem with logN complexity
# which is better than sqrtN since it grows slower
# https://stackoverflow.com/questions/42038294/is-complexity-ologn-equivalent-to-osqrtn
def two_crystal_balls_logn(breaks: List[bool]) -> int:
    # Note: an optional implementation of the problem with logn time complexity that wasn't even explained in the video
    ...
