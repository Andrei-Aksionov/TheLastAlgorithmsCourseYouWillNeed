from typing import Tuple

import pytest

from course.search.binary_search import binary_search


@pytest.mark.search
@pytest.mark.parametrize(
    "target",
    [
        (1, True),
        (8, False),
        (69, True),
        (1336, False),
        (69420, True),
        (69421, False),
    ],
)
def test_linear_search(target: Tuple[int, bool]) -> None:
    # Given
    haystack = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    needle, expected_result = target

    # When
    linear_search_result = binary_search(haystack, needle)

    # Then
    assert expected_result == linear_search_result
