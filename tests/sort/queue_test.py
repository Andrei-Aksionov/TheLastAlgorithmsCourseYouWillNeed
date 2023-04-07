import random
from typing import List

import pytest

from course.sort.queue import Queue
from course.utils import is_empty_class


@pytest.mark.sort
@pytest.mark.skipif(is_empty_class(Queue), reason="non implemented class Queue")
class TestQueue:
    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_queue_dequeue(self, numbers: List[int]) -> None:
        # Given
        queue = Queue()
        for number in numbers:
            queue.enqueue(number)

        # When
        head_value = queue.dequeue()

        # Then
        assert head_value == numbers[0]
        assert queue.length == len(numbers) - 1

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_queue_dequeue_with_peek(self, numbers: List[int]) -> None:
        queue = Queue()
        # add all numbers into the queue
        for number in numbers:
            queue.enqueue(number)
        # assert that the tail's value is equal to the last number
        assert queue.peek() == numbers[0]

        # delete all the elements in the queue
        for _ in numbers:
            queue.dequeue()
        assert queue.length == 0

        # after deletion add one more element
        new_number = random.randint(-100, 100)
        queue.enqueue(new_number)
        assert queue.peek() == new_number
        assert queue.length == 1

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_queue_emptied_head_tail_none(self, numbers: List[int]) -> None:
        queue = Queue()
        # add all numbers into the queue
        for number in numbers:
            queue.enqueue(number)

        # delete all the elements in the queue
        for _ in numbers:
            queue.dequeue()

        assert queue.head is None
        assert queue.tail is None

    @pytest.mark.parametrize("numbers", [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)])
    def test_queue_emptied_dequeue_return_none(self, numbers: List[int]) -> None:
        queue = Queue()
        # add all numbers into the queue
        for number in numbers:
            queue.enqueue(number)

        # delete all the elements in the queue
        for _ in numbers:
            queue.dequeue()

        assert queue.dequeue() is None

    def test_queue_empty_peek_return_none(self) -> None:
        queue = Queue()

        assert queue.peek() is None
