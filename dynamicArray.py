import math
from functools import reduce
from typing import TypeVar
from typing import Any, List, Callable

T = TypeVar("T", str, int, float)


def cons(arr: List[T], value: T) -> List[T]:
    """Add a new element."""
    new_arr = arr.copy()
    if value is not None:
        new_arr.append(value)
    return new_arr


def remove(arr: List[T], value: T) -> List[T]:
    """Remove an element by value."""
    if value is None:
        return arr
    new_arr: List[T] = []
    for i in range(len(arr)):
        if arr[i] != value:
            new_arr.append(arr[i])
    return new_arr


def length(arr: List[T]) -> int:
    """Return the size of the array."""
    return len(arr)


def member(arr: List[T], value: T) -> bool:
    """Check if the value is a member of the array."""
    flag = False
    for i in range(len(arr)):
        if arr[i] == value:
            flag = True
    return flag


def reverse(arr: List[T]) -> List[T]:
    """Reverse the array."""
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append(arr[i])
    return new_arr


def from_list(lst: List[T]) -> List[T]:
    """Conversion from list to DynamicArray."""
    arr = lst
    return arr


def to_list(arr: List[T]) -> List[T]:
    """Conversion from DynamicArray to list."""
    lst = arr
    return lst


def value_find_key(arr: List[T], value: T) -> int:
    """Find index by the value."""
    index = -1
    for i in range(len(arr)):
        if arr[i] == value:
            index = i
            break
    return index


def key_find_value(arr: List[T], key: int) -> T:
    """Find value by the index."""
    if (key is None) or (key < 0 or key >= len(arr)):
        raise IndexError("invalid index")
    return arr[key]

# 8. ﬁlter data structure by speciﬁc predicate


def is_odd(n: int) -> bool:
    """Check if n is odd."""
    if isinstance(n, int):
        return n % 2 == 1


def is_even(n: int) -> bool:
    """Check if n is even."""
    if isinstance(n, int):
        return n % 2 == 0


def filter_func(arr: List[T], fun: Callable[[T], T]) -> List[T]:
    """Filter elements by given function fun."""
    new_arr = list(filter(fun, arr))
    return new_arr

# 9. map structure by speciﬁc function


def square(x: int) -> int:
    """Calculate the square of x."""
    if isinstance(x, int):
        return x ** 2


def map_func(arr: List[T], fun: Callable[[T], T]) -> List[T]:
    """Map the elements in the array with the given function fun."""
    new_arr = list(map(fun, arr))
    return new_arr


def sum(x: T, y: T) -> T:
    """Calculate the sum of x and y."""
    return x + y


def reduce_func(arr: List[T], fun: Callable[[T, T], T]) -> T:
    """Reduce process elements and build a value by the function"""
    sum = reduce(fun, arr)
    return sum


def iterator(arr: List[T]) -> Callable[[], T]:
    """Function style iterator"""
    idx = 0

    def foo() -> T:
        nonlocal idx, arr
        len_arr = len(arr)
        if idx >= len_arr:
            raise StopIteration
        value = arr[idx]
        idx += 1
        return value
    return foo


def mempty(arr: List[T]) -> List[T]:
    """Set the DynamicArray to empty."""
    return []


def mconcat(arr: List[T], other_arr: List[T]) -> List[T]:
    """Concat two dynamic arrays."""
    tmp_arr = arr + other_arr
    return tmp_arr
