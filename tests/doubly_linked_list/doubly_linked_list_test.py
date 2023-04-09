import random
from typing import List

import pytest

from course.doubly_linked_list.doubly_linked_list import LinkedList
from course.utils import is_empty_class


@pytest.mark.doubly_linked_list
@pytest.mark.skipif(is_empty_class(LinkedList), reason="non implemented class LinkedList")
class TestLinkedList:
    def test_linked_list_all_combined(self) -> None:
        # This one is taken (and adopted for python) from the ThePrimeagen repo:
        # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/DoublyLinkedList.ts
        # that was used for testing in the video course

        # Given
        linked_list = LinkedList()

        # When
        linked_list.append(5)
        linked_list.append(7)
        linked_list.append(9)
        # Then
        assert linked_list.get(2) == 9
        assert linked_list.remove_at(1) == 7
        assert linked_list.length == 2

        # When
        linked_list.append(11)
        # Then
        assert linked_list.remove_at(1) == 9
        assert linked_list.remove(9) is None
        assert linked_list.remove_at(0) == 5
        assert linked_list.remove_at(0) == 11
        assert linked_list.length == 0

        # When
        linked_list.prepend(5)
        linked_list.prepend(7)
        linked_list.prepend(9)
        # Then
        assert linked_list.get(2) == 5
        assert linked_list.get(0) == 9
        assert linked_list.remove(9) == 9
        assert linked_list.length == 2
        assert linked_list.get(0) == 7

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_linked_list_append(self, numbers: List[int]) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.append(number)

        # Then
        assert linked_list.length == len(numbers)

    @pytest.mark.parametrize(
        ("numbers", "get_at"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_linked_list_get(self, numbers: List[int], get_at: int) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.append(number)

        # Then
        assert linked_list.length == len(numbers)
        assert linked_list.get(get_at) == numbers[get_at]

    @pytest.mark.parametrize(
        ("numbers", "remove_idx"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_linked_list_remove_at(self, numbers: List[int], remove_idx: int) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.append(number)

        # Then
        assert linked_list.length == len(numbers)
        assert linked_list.remove_at(remove_idx) == numbers[remove_idx]

    @pytest.mark.parametrize(
        ("numbers", "prepand_number"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_linked_list_prepend(self, numbers: List[int], prepand_number: int) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.append(number)

        linked_list.prepend(prepand_number)

        # Then
        assert linked_list.length == len(numbers) + 1
        assert linked_list.get(0) == prepand_number

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_linked_list_prepand_to_empty(self, numbers: List[int]) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.prepend(number)

        # Then
        assert linked_list.length == len(numbers)
        for idx in range(len(numbers)):
            assert linked_list.get(idx) == numbers[-idx - 1]

    @pytest.mark.parametrize(
        ("numbers", "value", "insert_idx"),
        list(
            zip(
                [random.sample(range(-100, 100), 25) for _ in range(10)],
                [random.randint(-100, 100) for _ in range(10)],
                [random.randint(0, 24) for _ in range(10)],
            ),
        ),
    )
    def test_linked_list_insert(self, numbers: List[int], value: int, insert_idx: int) -> None:
        # Given
        linked_list = LinkedList()

        # When
        for number in numbers:
            linked_list.append(number)

        linked_list.insert_at(value, insert_idx)

        # Then
        assert linked_list.length == len(numbers) + 1
        assert linked_list.get(insert_idx) == value
