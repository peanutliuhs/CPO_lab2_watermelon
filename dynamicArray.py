import math
from functools import reduce
from typing import Any, List, Callable


class DynamicArray(object):
    def __init__(self, *values: int) -> None:
        """DynamicArray constructor"""
        self._values = list(values)
        self._size = len(self._values)

    def __str__(self) -> str:
        """for str() implementation"""
        return str(self._values)

    def __eq__(self, other: Any) -> bool:
        """for write assertion, we should be abel for check list equality
        (list are equal, if all elements are equal).
        """
        if other is None:
            return False
        if self._values == other._values:
            return True
        else:
            return False


def cons(arr: DynamicArray, value: int) -> DynamicArray:
    """Add a new element."""
    if value is None:
        return arr
    else:
        new_arr = DynamicArray()
        new_arr._values = arr._values + [value]
        new_arr._size = len(new_arr._values)
    return new_arr


def remove(arr: DynamicArray, value: int) -> DynamicArray:
    """Remove an element by value."""
    if (value is None) or (arr._size == 0):
        return arr
    tmp_arr = DynamicArray()
    tmp_arr._values = arr._values[1:]
    tmp_arr._size = arr._size - 1
    if arr._values[0] == value:
        return tmp_arr
    else:
        new_arr = DynamicArray()
        new_arr._values = [arr._values[0]] + remove(tmp_arr, value)._values
        new_arr._size = arr._size - 1
        return new_arr


def length(arr: DynamicArray) -> int:
    """Return the size of the array."""
    return arr._size


def member(arr: DynamicArray, value: int) -> bool:
    """Check if the value is a member of the array."""
    if arr._size == 0:
        return False
    flag = False
    if arr._values[0] == value:
        flag = True
    else:
        tmp_arr = DynamicArray()
        tmp_arr._values = arr._values[1:]
        tmp_arr._size = arr._size - 1
        flag = member(tmp_arr, value)
    return flag


def reverse(arr: DynamicArray) -> DynamicArray:
    """Reverse the array."""
    new_arr = DynamicArray()
    if arr._size:
        tmp_arr = DynamicArray()
        tmp_arr._values = arr._values[:-1]
        tmp_arr._size = arr._size - 1
        new_arr._values = [arr._values[-1]] + reverse(tmp_arr)._values
        new_arr._size = arr._size
    return new_arr


def from_list(lst: List[int]) -> DynamicArray:
    """Conversion from list to DynamicArray."""
    arr = DynamicArray()
    arr._values = lst
    arr._size = len(lst)
    return arr


def to_list(arr: DynamicArray) -> List[int]:
    """Conversion from DynamicArray to list."""
    lst = arr._values
    return lst


def value_find_key(arr: DynamicArray, value: int) -> int:
    """Find index by the value."""
    if arr._size == 0:
        return -1
    if arr._values[0] == value:
        index = 0
    else:
        tmp_arr = DynamicArray()
        tmp_arr._values = arr._values[1:]
        tmp_arr._size = arr._size - 1
        index = value_find_key(tmp_arr, value) + 1
    return index


def key_find_value(arr: DynamicArray, key: int) -> int:
    """Find value by the index."""
    if (key is None) or (key < 0 or key >= arr._size):
        raise IndexError("invalid index")
    return arr._values[key]


def is_odd(n: int) -> bool:
    """Check if n is odd."""
    if isinstance(n, int):
        return n % 2 == 1


def is_even(n: int) -> bool:
    """Check if n is even."""
    if isinstance(n, int):
        return n % 2 == 0


def filter_func(arr: DynamicArray, fun: Callable[[int], int]) -> DynamicArray:
    """Filter elements by given function fun."""
    new_arr = DynamicArray()
    new_arr._values = list(filter(fun, arr._values))
    new_arr._size = len(new_arr._values)
    return new_arr


def square(x: int) -> int:
    """Calculate the square of x."""
    if isinstance(x, int):
        return x ** 2


def map_func(arr: DynamicArray, fun: Callable[[int], int]) -> DynamicArray:
    """Map the elements in the array with the given function fun."""
    new_arr = DynamicArray()
    new_arr._values = list(map(fun, arr._values))
    new_arr._size = len(new_arr._values)
    return new_arr


def sum(x: int, y: int) -> int:
    """Calculate the sum of x and y."""
    return x + y


def reduce_func(arr: DynamicArray, fun: Callable[[int, int], int]) -> int:
    """Reduce process elements and build a value by the function"""
    sum = reduce(fun, arr._values)
    return sum


def iterator(arr: DynamicArray) -> Callable[[], int]:
    """Function style iterator"""
    idx = 0

    def foo() -> int:
        nonlocal idx, arr
        len_arr = arr._size
        if idx >= len_arr:
            raise StopIteration
        value = arr._values[idx]
        idx += 1
        return value
    return foo


def mempty(arr: DynamicArray) -> DynamicArray:
    """Set the DynamicArray to empty."""
    return DynamicArray()


def mconcat(arr: DynamicArray, other_arr: DynamicArray) -> DynamicArray:
    """Concat two dynamic arrays."""
    new_arr = DynamicArray()
    new_arr._values = arr._values + other_arr._values
    new_arr._size = arr._size + other_arr._size
    return new_arr
