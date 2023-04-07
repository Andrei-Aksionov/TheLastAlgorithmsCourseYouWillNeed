import random
from typing import List

import pytest

from course.array.array_list import ArrayList
from course.utils import is_empty_class


@pytest.mark.array
@pytest.mark.skipif(is_empty_class(ArrayList), reason="non implemented class ArrayList")
class TestArrayList:
    def test_array_list_all_combined(self) -> None:
        # This one is taken (and adopted for python) from the ThePrimeagen repo:
        # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/ArrayList.ts
        # that was used for testing in the video course

        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        array_list.append(5)
        array_list.append(7)
        array_list.append(9)
        # Then
        assert array_list.get(2) == 9
        assert array_list.remove_at(1) == 7
        assert array_list.length == 2

        # When
        array_list.append(11)
        # Then
        assert array_list.remove_at(1) == 9
        assert array_list.remove(9) is None
        assert array_list.remove_at(0) == 5
        assert array_list.remove_at(0) == 11
        assert array_list.length == 0

        # When
        array_list.prepend(5)
        array_list.prepend(7)
        array_list.prepend(9)
        # Then
        assert array_list.get(2) == 5
        assert array_list.get(0) == 9
        assert array_list.remove(9) == 9
        assert array_list.length == 2
        assert array_list.get(0) == 7

    @pytest.mark.parametrize(
        ("numbers", "capacity"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(1, 25) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_capacity(self, numbers: List[int], capacity: int) -> None:
        # Given
        array_list = ArrayList(capacity=capacity, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        for idx in range(len(numbers)):
            assert array_list.get(idx) == numbers[idx]

    @pytest.mark.parametrize(
        ("numbers", "growth_value"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(1, 25) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_growth_value(self, numbers: List[int], growth_value: int) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=growth_value)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        for idx in range(len(numbers)):
            assert array_list.get(idx) == numbers[idx]

    @pytest.mark.parametrize(
        ("numbers", "capacity", "growth_value"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(1, 25) for _ in range(10)],
                [random.randint(1, 25) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_capacity_and_growth_value(self, numbers: List[int], capacity: int, growth_value: int) -> None:
        # Given
        array_list = ArrayList(capacity=capacity, growth_value=growth_value)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        for idx in range(len(numbers)):
            assert array_list.get(idx) == numbers[idx]

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_array_list_append(self, numbers: List[int]) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)

    @pytest.mark.parametrize(
        ("numbers", "get_at"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_get(self, numbers: List[int], get_at: int) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        assert array_list.get(get_at) == numbers[get_at]

    @pytest.mark.parametrize(
        ("numbers", "remove_at"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_remove_at(self, numbers: List[int], remove_at: int) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        assert array_list.remove_at(remove_at) == numbers[remove_at]

    @pytest.mark.parametrize(
        ("numbers", "prepand_number"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_array_list_prepand(self, numbers: List[int], prepand_number: int) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        array_list.prepend(prepand_number)

        # Then
        assert array_list.length == len(numbers) + 1
        assert array_list.get(0) == prepand_number

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_array_list_prepand_to_empty(self, numbers: List[int]) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.prepend(number)

        # Then
        assert array_list.length == len(numbers)
        for idx in range(len(numbers)):
            assert array_list.get(idx) == numbers[-idx - 1]

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_array_list_pop(self, numbers: List[int]) -> None:
        # Given
        array_list = ArrayList(capacity=3, growth_value=3)

        # When
        for number in numbers:
            array_list.append(number)

        # Then
        assert array_list.length == len(numbers)
        for expected_number in numbers[::-1]:
            assert array_list.pop() == expected_number
