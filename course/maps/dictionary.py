"""
Note: it's an optional algorithm that was explained in the course, but not implemented.

Attempt to implement python dictionary from scratch.
The implementation consists of two classes:
    - KeyValue: stores dictionary object
    - Dictionary: does all heavy-lifting like accessing/deleting values by keys.
"""


class KeyValue:
    def __init__(self, key: object, value: object = None) -> None:
        self.key = key
        self.value = value
        self.hash = self._hash()

    def __eq__(self, other: "KeyValue") -> bool:
        return self.key == other.key

    def _hash(self) -> int:
        # to better understand hashing it will be implemented from scratch
        # of course in real world it's better to use builtin hash function

        if isinstance(self.key, str):
            return sum(map(ord, self.key))
        # if it's not a string rollback to a builtin hash function
        return hash(self.key)

    def __repr__(self) -> str:
        return f"{self.key} : {self.value}"


class Dictionary:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def get(self, key: object, default: object = None) -> object:
        """Return value by provided key, default if not found.

        Parameters
        ----------
        key : object
            the keyname of the item you want to return.
        value : object
            a value to return if the specified key does not exist.
        """

        key_value = KeyValue(key)
        bucket = self.buckets[key_value.hash % self.size]
        for key_value in bucket:
            if key_value.key == key:
                return key_value.value
        return default

    def __getitem__(self, key: object) -> object:
        value = self.get(key)
        if not value:
            raise KeyError(f"Key {key} not found.")
        return value

    def __setitem__(self, key: object, value: object) -> None:
        new_key_value = KeyValue(key, value)
        bucket = self.buckets[new_key_value.hash % self.size]
        for bucket_key_value in bucket:
            if bucket_key_value.key == new_key_value.key:
                bucket.remove(bucket_key_value)
                break
        bucket.append(new_key_value)

    def pop(self, key: object, default: object = None) -> object:
        """Delete item from dictionary and return it.

        Parameters
        ----------
        key : object
            the keyname of the item you want to delete.
        value : object
            a value to return if the specified key does not exist.
        """

        target_key_value = KeyValue(key)
        bucket = self.buckets[target_key_value.hash % self.size]
        for bucket_key_value in bucket:
            if bucket_key_value.key == target_key_value.key:
                value = bucket_key_value.value
                bucket.remove(bucket_key_value)
                return value
        return default
