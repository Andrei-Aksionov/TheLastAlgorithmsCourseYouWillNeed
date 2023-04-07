"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

In Python a regular List is essentially an ArrayList from Typescript.
But for the sake of practicing algorithms let's pretend that this is not
the case and implement the logic manually.

To run tests: python -m arrays
"""


from typing import Optional


class ArrayList:
    """
    -----------------------------
    |   A  |   B  | None | None |
    -----------------------------
               ↑             ↑
             length       capacity
    """

    def __init__(self, capacity: int, growth_value: int) -> None:
        self.array = [None] * capacity
        self.length = 0
        self.capacity = capacity
        # when there is no space in the buffer to add new value
        # a new array will be created with size of current one + growth_value
        # and all values will be copied from current array into the new one
        self.growth_value = growth_value

    def get(self, idx: int) -> int:
        if idx >= self.length:
            raise ValueError(f"Index out of bounds: limit is {self.length - 1}")
        return self.array[idx]

    def append(self, value: int) -> None:
        """Append a value to the end of the array."""
        self.update_sizing()
        self.array[self.length] = value
        self.length += 1

    def prepend(self, value: int) -> None:
        """Add value to the beginning of the array."""
        self.insert(value, 0)

    def insert(self, value: int, pos: int) -> None:
        """Insert value into a specified position."""
        if pos < 0:
            raise ValueError("Negative positions are not supported.")
        if pos >= self.capacity:
            raise ValueError("You are trying to insert value at the position that is out of capacity boundaries.")
        pos = min(self.length, pos)
        self.update_sizing()
        # make a space for the new value by shifting all current
        # vales of the array up to position
        for idx in range(self.length, pos, -1):
            self.array[idx] = self.array[idx - 1]
        self.array[pos] = value
        self.length += 1

    def pop(self) -> int:
        """Delete and display the last element of the array."""
        self.length -= 1
        value = self.array[self.length]
        self.update_sizing()
        return value

    def remove_at(self, pos: int) -> int:
        """Remove value at a specified position."""
        if pos < 0:
            raise ValueError("Negative positions are not supported.")
        if not 0 <= pos < self.length:
            raise ValueError("You are trying to remove value at the position that is out of boundaries.")
        value_to_remove = self.array[pos]
        # fill up place where the value to be deleted currently is
        # by shifting values of the array
        for idx in range(pos, self.length - 1):
            self.array[idx] = self.array[idx + 1]
        self.length -= 1
        self.update_sizing()
        return value_to_remove

    def remove(self, value: int) -> Optional[int]:
        """Remove specified value without providing position."""
        # Find value's position within the array
        for idx in range(self.length):
            if self.array[idx] == value:
                break
        # If the value is not in the array - return None
        if idx >= self.length - 1:
            return None
        return self.remove_at(idx)

    def update_sizing(self) -> None:
        """Check whether we should increase or decrease the size of array."""
        recreate_flag = False
        # if there is no space to add a new element
        if self.length >= self.capacity:
            self.capacity = self.capacity + self.growth_value
            recreate_flag = True

        # if there are too many empty spaces
        elif self.length < self.capacity - self.growth_value:
            self.capacity = self.length + self.growth_value
            recreate_flag = True

        # create new array and copy elements from the old one
        if recreate_flag:
            new_array = [None] * self.capacity
            for idx in range(self.length):
                new_array[idx] = self.array[idx]
            self.array = new_array
