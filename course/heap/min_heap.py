"""
To run tests: python -m heap
"""


class MinHeap:
    """
                               Min Heap

                  Values                           Indices

                    50                                0
                 /      \                           /    \
              71          100                     1        2
            /    \        /  \                  /  \      /  \
          101    80     200   105              3    4    5    6
          /                                   /
         106                                 7

    Values:  [50, 71, 100, 101, 80, 200, 105, 106]
    Indices: [0,  1,  2,   3,   4,  5,   6,   7]

          parent
            |
        [(i-1)/2]
            |
          _____
          |   |
          -----
        /       \
      2i+1     2i+2
      /           \
    left          right
    child         child

    """

    def __init__(self) -> None:
        self.data = []
        self.length = 0

    def insert(self, value: int) -> None:
        "Insert the new value into the min heap."
        # Note: time and space complexities are the same for:
        #   - insert/delete
        #   - heapify_up/heapify_down
        # Time: O(logn) because the structure is a complete tree,
        # which means that it's balanced
        # Space: O(1) for iterative solution, O(logn) for recursive

        # after adding the new value to the end of the heap
        # we need to find where it belongs in the MinHeap
        self.data.append(value)
        self._heapify_up(self.length)
        self.length += 1

    def delete(self) -> int:
        """Deletes the first element."""

        if self.length == 0:
            raise ValueError("You are trying to delete from an empty heap.")

        deleted_value = self.data[0]
        # put the last element in the begginning
        self.data[0] = self.data[self.length - 1]
        # remove the last element
        self.data.pop()
        # don't forget to update length
        self.length -= 1
        # now the last (most likely the largest) value is in the beginning of the MinHeap
        # we need to find a more suitable place for it
        self._heapify_down(0)
        # and return deleted value (originally was in the beginning of the heap)
        return deleted_value

    def _heapify_up(self, child_idx: int) -> None:
        """Move smaller then parent value to the top.

        The code below uses recursive approach as in the video.
        Iterative is not much uglier, but it's more performant.

        ```python
            if child_idx <= 0:
                return

            parent_idx = self._parent(child_idx)
            parent_value = self.data[parent_idx]
            child_value = self.data[child_idx]
            if parent_value > child_value:
                self.data[parent_idx] = child_value
                self.data[child_idx] = parent_value
            self._heapify_up(parent_idx)
        ```
        """

        while child_idx > 0:
            parent_idx = self._parent(child_idx)
            parent_value = self.data[parent_idx]
            child_value = self.data[child_idx]
            if parent_value <= child_value:
                break
            self.data[parent_idx] = child_value
            self.data[child_idx] = parent_value
            child_idx = parent_idx

    def _heapify_down(self, parent_idx: int) -> None:
        """Move larger then parent value to the buttom.

        The code below uses recursive approach as in the video.
        Iterative is not much uglier, but it's more performant.

        ```python
            if parent_idx >= self.length:
                return

            left_idx = self._left_child(parent_idx)
            right_idx = self._right_child(parent_idx)
            left_value = self.data[left_idx] if left_idx < self.length else float("inf")
            right_value = self.data[right_idx] if right_idx < self.length else float("inf")

            parent_value = self.data[parent_idx]
            child_idx = left_idx if left_value < right_value else right_idx
            child_value = min(left_value, right_value)

            if parent_value > child_value:
                self.data[parent_idx] = child_value
                self.data[child_idx] = parent_value
                self._heapify_down(child_idx)
        ```
        """
        while parent_idx < self.length:
            left_idx = self._left_child(parent_idx)
            right_idx = self._right_child(parent_idx)
            left_value = self.data[left_idx] if left_idx < self.length else float("inf")
            right_value = self.data[right_idx] if right_idx < self.length else float("inf")

            parent_value = self.data[parent_idx]
            child_idx = left_idx if left_value < right_value else right_idx
            child_value = min(left_value, right_value)

            if parent_value <= child_value:
                break
            self.data[parent_idx] = child_value
            self.data[child_idx] = parent_value
            self._heapify_down(child_idx)
            parent_idx = child_idx

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left_child(self, idx: int) -> int:
        return 2 * idx + 1

    def _right_child(self, idx: int) -> int:
        return 2 * idx + 2
