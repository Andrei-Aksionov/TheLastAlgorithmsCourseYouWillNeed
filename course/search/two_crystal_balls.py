from typing import List


def two_crystal_balls(breaks: List[bool]) -> int:
    # O(sqrtN) time | O(1) space
    # but for me it looks more like O(n/sqrtN + sqrtN) time

    # find size of the jump (sqrt of the list)
    jump_amount = int(len(breaks) ** 0.5)

    # jump every sqrt items till we find True value
    for i in range(0, len(breaks), jump_amount):
        if breaks[i]:
            break

    # when we find True value, that means that the first True value is in the
    # current sqrt-size block. Now we need to go back (to the beginning of the block)
    # and iterate over the whole block until we find the first True value

    # go back sqrt-size items back only if we found True value
    # if not - no necessity to move
    if breaks[i]:
        i = max(0, i - jump_amount)

    # find the first True value in the sqrt-size block
    for j in range(i, min(i + jump_amount + 1, len(breaks))):
        if breaks[j]:
            return j

    return -1


# it is possible to solve that exact problem with logN complexity
# which is better than sqrtN since it grows slower
# https://stackoverflow.com/questions/42038294/is-complexity-ologn-equivalent-to-osqrtn
def two_crystal_balls_logn(breaks: List[bool]) -> int:
    # O(logN) time | O(1) space

    left, right = 0, len(breaks) - 1
    last_known = -1  # contains last time we saw True value

    while left <= right:
        middle = (left + right) // 2
        if breaks[middle]:
            # if it's already True, then the first True will be to the left
            # [..., ..., True, True, True, ..., ...]
            #                    ↑
            #                  middle
            last_known = middle
            right = middle - 1
        else:
            # in other case the first True is to the right
            # [..., False, False, False, ..., ..., True, True]
            #                ↑
            #              middle
            left = middle + 1

    # if we never saw True value, the default `-1` will be returned
    return last_known
