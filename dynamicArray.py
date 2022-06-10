import math
from functools import reduce
from typing import TypeVar, Generic
from typing import Any, List, Callable


T = TypeVar('T')
T2 = TypeVar('T2', None, int, float, str)


class DynamicArray(Generic[T]):
    def __init__(self, *values: T) -> None:
        """DynamicArray constructor"""
        self._values = list(values)
        self._size = len(self._values)

    def __str__(self) -> str:
        """for str() implementation"""
        return str(self._values)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DynamicArray):
            return False
        return self._values == other._values


def cons(arr: DynamicArray[T2], value: T2) -> DynamicArray[T2]:
    """Add a new element."""
    if value is None:
        return arr
    else:
        new_arr: DynamicArray[T2] = DynamicArray()
        new_arr._values = arr._values + [value]
        new_arr._size = len(new_arr._values)
    return new_arr


def remove(arr: DynamicArray[T2], value: T2) -> DynamicArray[T2]:
    """Remove an element by value."""
    if (value is None) or (arr._size == 0):
        return arr
    tmp_arr: DynamicArray[T2] = DynamicArray()
    tmp_arr._values = arr._values[1:]
    tmp_arr._size = arr._size - 1
    if arr._values[0] == value:
        return tmp_arr
    else:
        new_arr: DynamicArray[T2] = DynamicArray()
        new_arr._values = [arr._values[0]] + remove(tmp_arr, value)._values
        new_arr._size = arr._size - 1
        return new_arr


def length(arr: DynamicArray[T2]) -> int:
    """Return the size of the array."""
    return arr._size


def member(arr: DynamicArray[T2], value: T2) -> bool:
    """Check if the value is a member of the array."""
    if arr._size == 0:
        return False
    flag = False
    if arr._values[0] == value:
        flag = True
    else:
        tmp_arr: DynamicArray[T2] = DynamicArray()
        tmp_arr._values = arr._values[1:]
        tmp_arr._size = arr._size - 1
        flag = member(tmp_arr, value)
    return flag


def reverse(arr: DynamicArray[T2]) -> DynamicArray[T2]:
    """Reverse the array."""
    new_arr: DynamicArray[T2] = DynamicArray()
    if arr._size:
        tmp_arr: DynamicArray[T2] = DynamicArray()
        tmp_arr._values = arr._values[:-1]
        tmp_arr._size = arr._size - 1
        new_arr._values = [arr._values[-1]] + reverse(tmp_arr)._values
        new_arr._size = arr._size
    return new_arr


def from_list(lst: List[T2]) -> DynamicArray[T2]:
    """Conversion from list to DynamicArray."""
    arr: DynamicArray[T2] = DynamicArray()
    arr._values = lst
    arr._size = len(lst)
    return arr


def to_list(arr: DynamicArray[T2]) -> List[T2]:
    """Conversion from DynamicArray to list."""
    lst = arr._values
    return lst


def value_find_key(arr: DynamicArray[T2], value: T2) -> int:
    """Find index by the value."""
    if arr._size == 0:
        return -1
    if arr._values[0] == value:
        index = 0
    else:
        tmp_arr: DynamicArray[T2] = DynamicArray()
        tmp_arr._values = arr._values[1:]
        tmp_arr._size = arr._size - 1
        index = value_find_key(tmp_arr, value) + 1
    return index


def key_find_value(arr: DynamicArray[T2], key: int) -> T2:
    """Find value by the index."""
    if (key is None) or (key < 0 or key >= arr._size):
        raise IndexError("invalid index")
    return arr._values[key]


def is_odd(n: T2) -> bool:
    """Check if n is odd."""
    if isinstance(n, int):
        return n % 2 == 1
    else:
        return False


def is_even(n: T2) -> bool:
    """Check if n is even."""
    if isinstance(n, int):
        return n % 2 == 0
    else:
        return False


def filter_func(arr: DynamicArray[T2], fun: Callable[[T2], T2]) -> DynamicArray[T2]:
    """Filter elements by given function fun."""
    new_arr: DynamicArray[T2] = DynamicArray()
    new_arr._values = list(filter(fun, arr._values))
    new_arr._size = len(new_arr._values)
    return new_arr


def square(x: T2) -> int:
    """Calculate the square of x."""
    if isinstance(x, int):
        return x ** 2
    else:
        return -1


def map_func(arr: DynamicArray[T2], fun: Callable[[T2], T2]) -> DynamicArray[T2]:
    """Map the elements in the array with the given function fun."""
    new_arr: DynamicArray[T2] = DynamicArray()
    new_arr._values = list(map(fun, arr._values))
    new_arr._size = len(new_arr._values)
    return new_arr


def sum(x: T2, y: T2) -> int:
    """Calculate the sum of x and y."""
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return 0


def reduce_func(arr: DynamicArray[T2], fun: Callable[[T2, T2], T2]) -> T2:
    """Reduce process elements and build a value by the function"""
    sum = reduce(fun, arr._values)
    return sum


def iterator(arr: DynamicArray[T2]) -> Callable[[], T2]:
    """Function style iterator"""
    idx = 0

    def foo() -> T2:
        nonlocal idx, arr
        len_arr = arr._size
        if idx >= len_arr:
            raise StopIteration
        value = arr._values[idx]
        idx += 1
        return value
    return foo


def mempty(arr: DynamicArray[T2]) -> DynamicArray[T2]:
    """Set the DynamicArray to empty."""
    return DynamicArray()


def mconcat(arr: DynamicArray[T2], other_arr: DynamicArray[T2]) -> DynamicArray[T2]:
    """Concat two dynamic arrays."""
    new_arr: DynamicArray[T2] = DynamicArray()
    new_arr._values = arr._values + other_arr._values
    new_arr._size = arr._size + other_arr._size
    return new_arr
