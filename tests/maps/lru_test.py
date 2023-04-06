import random
from typing import List

import pytest

from course.maps.lru import LRU


@pytest.mark.map
def test_lru_cache() -> None:
    # This one is taken (and adopted for python) from the ThePrimeagen repo:
    # https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/LRU.ts
    # that was used for testing in the video course

    lru = LRU(capacity=3)
    assert lru.length == 0
    assert lru.capacity == 3

    assert lru.get("foo") is None
    # add new node
    lru.update("foo", 69)
    assert lru.get("foo") == 69
    assert lru.length == 1

    # add new node
    lru.update("bar", 420)
    assert lru.get("bar") == 420
    assert lru.length == 2

    # add new node
    lru.update("baz", 1337)
    assert lru.get("baz") == 1337
    assert lru.length == 3

    # add new node
    lru.update("ball", 69420)
    assert lru.length == 3
    assert lru.get("ball") == 69420
    assert lru.get("foo") is None
    assert lru.get("bar") == 420
    # update existing node
    lru.update("foo", 69)
    assert lru.length == 3
    assert lru.get("bar") == 420
    assert lru.get("foo") == 69

    # shouldn't of been deleted, but since bar was get'd, bar was added to the
    # front of the list, so baz became the end
    assert lru.get("baz") is None
    assert lru.length == 3


@pytest.mark.map
@pytest.mark.parametrize(
    ("values", "keys", "capacity"),
    list(
        zip(
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.randint(1, 5) for _ in range(10)],
        ),
    ),
)
def test_lru_length_does_not_exceed_capacity(values: List[int], keys: List[int], capacity: int) -> None:
    # Given
    lru = LRU(capacity)

    # When
    for value, key in zip(values, keys):
        lru.update(value, key)

    # Then
    assert lru.length <= capacity


@pytest.mark.map
@pytest.mark.parametrize(
    ("values", "keys", "capacity", "new_value"),
    list(
        zip(
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.randint(1, 5) for _ in range(10)],
            [random.randint(-100, 100) for _ in range(10)],
        ),
    ),
)
def test_lru_update_nodes_value(values: List[int], keys: List[int], capacity: int, new_value: int) -> None:
    # Given
    lru = LRU(capacity)

    # When
    for value, key in zip(values, keys):
        lru.update(value, key)

    lru.update(keys[-1], new_value)

    # Then
    assert lru.get(keys[-1]) == new_value


@pytest.mark.map
@pytest.mark.parametrize(
    ("values", "keys", "capacity"),
    list(
        zip(
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.randint(2, 5) for _ in range(10)],
        ),
    ),
)
def test_lru_get_value_will_not_be_dropped(values: List[int], keys: List[int], capacity: int) -> None:
    # Given
    lru = LRU(capacity)

    # When
    for value, key in zip(values, keys):
        lru.update(key, value)
        # constantly updating and pushing the first key-value so it should not be deleted
        lru.get(keys[0])

    # Then
    assert lru.get(keys[0]) is not None


@pytest.mark.map
@pytest.mark.parametrize(
    ("values", "keys", "capacity", "new_value"),
    list(
        zip(
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.sample(range(-100, 100), random.randint(1, 25)) for _ in range(10)],
            [random.randint(2, 5) for _ in range(10)],
            [random.randint(-100, 100) for _ in range(10)],
        ),
    ),
)
def test_lru_update_existing_value(values: List[int], keys: List[int], capacity: int, new_value: int) -> None:
    # Given
    lru = LRU(capacity)

    # When
    for value, key in zip(values, keys):
        lru.update(key, value)

    lru.update(keys[-1], new_value)

    # Then
    assert lru.get(keys[-1]) == new_value
