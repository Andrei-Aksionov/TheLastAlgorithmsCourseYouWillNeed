"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

In Python a regular List is essentially an ArrayList from Typescript.
But for the sake of practicing algorithms let's pretend that this is not
the case and implement the logic manually.

To run tests: pytest -m arrays
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
        # when there is no space left in the buffer to add a new value
        # a new array will be created with size of current one + growth_value
        # and all values will be copied from current array into the new one
        self.growth_value = growth_value

    def get(self, idx: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if idx >= self.length:
            raise ValueError(f"Index out of bounds: limit is {self.length - 1}")
        return self.array[idx]

    def append(self, value: int) -> None:
        """Append a value to the end of the array."""
        # Time: O(n) if there is a buffer then O(1), but if not O(n)
        #   since we need to create a new array of a bigger size and copy everything
        #   from current array into a new one
        # Space: O(n) the same as above
        self.update_sizing()
        self.array[self.length] = value
        self.length += 1

    def prepend(self, value: int) -> None:
        """Add value to the beginning of the array."""
        # Time: O(n) move all elements by 1 element to the right to make a free space
        # Space: O(n) if there is no buffer we need to create a new bigger array and copy into it
        self.insert(value, 0)

    def insert(self, value: int, pos: int) -> None:
        """Insert value into a specified position."""
        if pos < 0:
            raise ValueError("Negative positions are not supported.")
        if pos >= self.capacity:
            raise ValueError("You are trying to insert value at the position that is out of capacity boundaries.")
        pos = min(self.length, pos)
        self.update_sizing()
        # make a space for the new value by shifting all values from `pos` to the end of the array
        for idx in range(self.length, pos, -1):
            self.array[idx] = self.array[idx - 1]
        self.array[pos] = value
        self.length += 1

    def pop(self) -> int:
        """Delete and display the last element of the array."""
        # Time: O(n) since we need to create a smaller array and copy value into it in case there
        #   are too many empty spaces in the array
        #   Note: if to implement array_list without this housekeeping and simply return the last
        #   element then of course time complexity is O(1)
        # Space: O(n) create new array of a smaller size and copy into it
        self.length -= 1
        value = self.array[self.length]
        self.update_sizing()
        return value

    def remove_at(self, pos: int) -> int:
        """Remove value at a specified position."""

        # Time: O(n) after deleting an element at the provided position we need to
        #   fill up an empty space by shifting elements from right to left
        # Space: O(1)-O(n) depending on the implementation: if to shrink down empty spaces
        #   then O(n), if not - O(1)

        if pos < 0:
            raise ValueError("Negative positions are not supported.")
        if not 0 <= pos < self.length:
            raise ValueError("You are trying to remove value at the position that is out of boundaries.")
        value_to_remove = self.array[pos]
        # fill up place where the value to be deleted currently is by shifting values of the array
        for idx in range(pos, self.length - 1):
            self.array[idx] = self.array[idx + 1]
        self.length -= 1
        self.update_sizing()
        return value_to_remove

    def remove(self, value: int) -> Optional[int]:
        """Remove specified value without providing position."""

        # Time: O(n) iterate over all elements until matching value is found and then do `remove_at` which is also O(n)
        # Space: O(1)-O(n) depending on the implementation of `remove_at`

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

        # Time: O(n) if there is a need for shrinking/enlarging the array we need
        #   to create a new one and copy elements into it
        # Space: O(n) there same as for time complexity

        recreate_flag = False
        # if there is no space to add a new element
        if self.length >= self.capacity:
            self.capacity = self.capacity + self.growth_value
            recreate_flag = True

        # if there are too many empty spaces
        elif self.length < self.capacity - self.growth_value:
            self.capacity = self.length + self.growth_value
            recreate_flag = True

        # create a new array and copy elements from the old one
        if recreate_flag:
            new_array = [None] * self.capacity
            for idx in range(self.length):
                new_array[idx] = self.array[idx]
            self.array = new_array
