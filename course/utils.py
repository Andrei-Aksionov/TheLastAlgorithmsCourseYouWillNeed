from typing import Callable


def is_empty_function(func: Callable) -> bool:
    """Return True if provided function has an empty body."""

    def empty_func() -> None:
        pass

    def empty_func_with_doc() -> None:
        """Empty function with docstring."""

    return (
        func.__code__.co_code == empty_func.__code__.co_code
        or func.__code__.co_code == empty_func_with_doc.__code__.co_code
    )


def is_empty_class(_class: object) -> bool:
    """Return True if provided class has no implemented methods."""
    return all(bool(attribute.startswith("__")) for attribute in _class.__dict__)
