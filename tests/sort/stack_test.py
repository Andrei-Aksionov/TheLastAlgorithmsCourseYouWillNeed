import random
from typing import List

import pytest

from course.sort.stack import Stack


@pytest.mark.sort
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_queue_pop(numbers: List[int]) -> None:
    # Given
    stack = Stack()
    for number in numbers:
        stack.push(number)

    # When
    tail_value = stack.pop()

    # Then
    assert tail_value == numbers[-1]
    assert stack.length == len(numbers) - 1


@pytest.mark.sort
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_queue_pop_with_peek(numbers: List[int]) -> None:
    stack = Stack()
    # add all numbers into the queue
    for number in numbers:
        stack.push(number)
    # assert that the tail's value is equal to the last number
    assert stack.peek() == numbers[-1]

    # delete all the elements in the queue
    for _ in numbers:
        stack.pop()
    assert stack.length == 0

    # after deletion add one more element
    new_number = random.randint(-100, 100)
    stack.push(new_number)
    assert stack.peek() == new_number
    assert stack.length == 1


@pytest.mark.sort
@pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
def test_queue_emptied_head_tail_none(numbers: List[int]) -> None:
    stack = Stack()
    # add all numbers into the queue
    for number in numbers:
        stack.push(number)

    # delete all the elements in the queue
    for _ in numbers:
        stack.pop()

    assert stack.head is None


@pytest.mark.sort
def test_queue_empty_peek_return_none() -> None:
    stack = Stack()

    assert stack.peek() is None
