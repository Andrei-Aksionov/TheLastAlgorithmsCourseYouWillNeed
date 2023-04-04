import heapq
import random
from typing import List

import pytest

from course.heap.min_heap import MinHeap


@pytest.mark.heap
def test_min_heap_all_combined() -> None:
    # This one is taken (and adopted for python) from the ThePrimeagen repo:
    # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/MinHeap.ts
    # that was used for testing in the video course

    heap = MinHeap()

    assert heap.length == (0)

    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert heap.length == 8
    assert heap.delete() == 1
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert heap.length == 4
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == 69
    assert heap.delete() == 420
    assert heap.length == 0

    heap.insert(3)
    heap.insert(1)

    assert heap.length == 2
    assert heap.delete() == 1
    assert heap.delete() == 3


@pytest.mark.heap
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_min_heap_insert(numbers: List[int]) -> None:
    # Given
    heap = MinHeap()

    # When
    for number in numbers:
        heap.insert(number)

    # Then
    assert heap.length == len(numbers)
    assert sorted(heap.data) == sorted(numbers)


@pytest.mark.heap
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_min_heap_insert_delete(numbers: List[int]) -> None:
    # Given
    heap = MinHeap()

    # When
    for number in numbers:
        heap.insert(number)

    for _ in numbers:
        heap.delete()

    # Then
    assert heap.length == 0


@pytest.mark.heap
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_min_heap_insert_delete_insert(numbers: List[int]) -> None:
    # Given
    heap = MinHeap()

    # When
    for number in numbers:
        heap.insert(number)
    for _ in numbers:
        heap.delete()
    for number in numbers:
        heap.insert(number)

    # Then
    assert heap.length == len(numbers)
    assert sorted(heap.data) == sorted(numbers)


@pytest.mark.heap
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_min_heap_compare_pop_with_builtin(numbers: List[int]) -> None:
    # Given
    heap = MinHeap()

    # When
    for number in numbers:
        heap.insert(number)

    # transform `numbers` in-place into min-heap with builtin heapq library
    heapq.heapify(numbers)

    # Then
    for _ in numbers:
        assert heap.delete() == heapq.heappop(numbers)
