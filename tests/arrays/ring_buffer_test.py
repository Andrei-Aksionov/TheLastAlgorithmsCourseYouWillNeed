import random
from typing import List

import pytest

from course.arrays.ring_buffer import RingBuffer
from course.utils import is_empty_class


@pytest.mark.arrays
@pytest.mark.skipif(is_empty_class(RingBuffer), reason="non implemented class RingBuffer")
class TestRingBuffer:
    def test_ring_buffer_all_combined(self) -> None:
        # This one is taken (and adopted for python) from the ThePrimeagen repo:
        # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/ArrayList.ts
        # that was used for testing in the video course

        buffer = RingBuffer(capacity=5)

        buffer.push(5)
        assert buffer.pop() == 5
        assert buffer.pop() is None

        buffer.push(42)
        buffer.push(9)
        assert buffer.pop() == 9
        assert buffer.pop() == 42
        assert buffer.pop() is None

        buffer.push(42)
        buffer.push(9)
        buffer.push(12)
        assert buffer.get(2) == 12
        assert buffer.get(1) == 9
        assert buffer.get(0) == 42

    def test_ring_buffer_with_overwrite(self) -> None:
        # Given
        buffer = RingBuffer(capacity=5)

        # When
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.push(6)
        # after [1, 2, 3, 4, 5] when adding new number it will exceed capacity of 5
        # so after adding 6 the buffer should contain [6, 2, 3, 4, 5]
        # because 6 instead of being added after 5 was placed where previously 1 was
        # Note: the oldest value is 2, the latest value is 6

        # Then
        for expected_number in [6, 5, 4, 3, 2]:
            assert buffer.pop() == expected_number

    def test_ring_buffer_get_with_overwrite(self) -> None:
        # Given
        buffer = RingBuffer(capacity=5)

        # When
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.push(6)

        # Then
        for idx, expected_number in enumerate([2, 3, 4, 5, 6]):
            assert buffer.get(idx) == expected_number

    def test_ring_buffer_pop_get_with_overwrite(self) -> None:
        # Given
        buffer = RingBuffer(capacity=5)

        # When
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.push(6)

        for _ in range(6):
            buffer.pop()

        buffer.push(1)
        buffer.push(2)
        buffer.push(3)

        # Then
        for idx, expected_number in enumerate([1, 2, 3]):
            assert buffer.get(idx) == expected_number

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), 25) for _ in range(10)])
    def test_ring_buffer_with_overwrite_auto(self, numbers: List[int]) -> None:
        # Given
        buffer = RingBuffer(capacity=5)

        # When
        for number in numbers:
            buffer.push(number)

        # Then
        for expected_number in numbers[:-6:-1]:
            assert buffer.pop() == expected_number

    @pytest.mark.parametrize(
        ("numbers", "capacity"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(3, 25) for _ in range(10)],
            ),
        ),
    )
    def test_ring_buffer_with_overwrite_capacity_auto(self, numbers: List[int], capacity: int) -> None:
        # Given
        buffer = RingBuffer(capacity=capacity)

        # When
        for number in numbers:
            buffer.push(number)

        # Then
        for expected_number in numbers[: -(capacity + 1) : -1]:
            assert buffer.pop() == expected_number

    @pytest.mark.parametrize(
        ("numbers", "capacity"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(3, 25) for _ in range(10)],
            ),
        ),
    )
    def test_ring_buffer_push_pop_push_auto(self, numbers: List[int], capacity: int) -> None:
        # Given
        buffer = RingBuffer(capacity=capacity)

        # When
        for number in numbers:
            buffer.push(number)
        for _ in numbers:
            buffer.pop()
        for number in numbers:
            buffer.push(number)

        # Then
        for expected_number in numbers[: -(capacity + 1) : -1]:
            assert buffer.pop() == expected_number
