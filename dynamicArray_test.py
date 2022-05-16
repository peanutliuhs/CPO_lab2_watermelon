import unittest
from dynamicArray import *
from hypothesis import given
import hypothesis.strategies as st
from typing import List


class TestDynamicArray(unittest.TestCase):

    def test_cons(self) -> None:
        arr: List[int] = []
        self.assertEqual(cons(arr, None), arr)
        self.assertEqual(cons(cons(arr, None), None), arr)
        self.assertEqual(cons(arr, 1), [1])
        self.assertEqual(cons(cons(arr, 1), 4), [1, 4])

    def test_remove(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(remove(arr, None), arr)
        self.assertEqual(remove(arr, 1), [4, 5, 3])
        self.assertEqual(remove(remove(arr, 1), 3), [4, 5])

    def test_length(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(length(arr), 4)

    def test_member(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(member(arr, -1), False)
        self.assertEqual(member(arr, 5), True)

    def test_reverse(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(reverse(arr), [3, 5, 4, 1])

    def test_from_list(self) -> None:
        lst = [1, 4, 5, 3]
        self.assertEqual(from_list([1, 4, 5, 3]), lst)

    def test_to_list(self) -> None:
        self.assertEqual(to_list([]), [])
        lst = [1, 4, 5, 3]
        self.assertEqual(to_list(lst), [1, 4, 5, 3])

    def test_find(self) -> None:
        arr1: List[int] = []
        self.assertEqual(value_find_key(arr1, 0), -1)
        self.assertEqual(value_find_key(arr1, 1), -1)
        arr2 = [1, 4, 5, 3]
        self.assertEqual(value_find_key(arr2, 5), 2)
        self.assertEqual(key_find_value(arr2, 1), 4)

    def test_ﬁlter(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(filter_func(arr, is_odd), [1, 5, 3])
        self.assertEqual(filter_func(arr, is_even), [4])

    def test_map(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(map_func(arr, square), [1, 16, 25, 9])

    def test_reduce(self) -> None:
        arr = [1, 4, 5, 3]
        self.assertEqual(reduce_func(arr, sum), 13)

    def test_iter(self) -> None:
        arr1 = [1, 4, 5, 3]
        arr2 = [1, 4, 5, 3]
        get_next1 = iterator(arr1)
        get_next2 = iterator(arr2)
        self.assertEqual(get_next1(), 1)
        self.assertEqual(get_next2(), 1)
        self.assertEqual(get_next1(), 4)
        self.assertEqual(get_next2(), 4)
        self.assertEqual(get_next1(), get_next2())

    def test_mempty(self) -> None:
        self.assertEqual(mempty([]), cons([], None))
        self.assertEqual(mempty([1, 4, 5, 3]), cons([], None))

    def test_mconcat(self) -> None:
        arr = [1, 4]
        self.assertEqual(mconcat([], []), cons([], None))
        self.assertEqual(mconcat([], arr), arr)
        self.assertEqual(mconcat(arr, [5, 3]), cons(
            cons(cons(cons([], 1), 4), 5), 3))

    @given(st.lists(st.integers()))
    def test_from_list_to_list(self, lst: List[T]) -> None:
        arr = from_list(lst)
        tmp_arr = to_list(lst)
        self.assertEqual(lst, tmp_arr)

    @given(st.lists(st.integers()))
    def test_len_size(self, lst: List[T]) -> None:
        arr = from_list(lst)
        self.assertEqual(length(arr), len(lst))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, arr: List[T]) -> None:
        self.assertEqual(mconcat(mempty([]), arr), arr)
        self.assertEqual(mconcat(arr, mempty([])), arr)
        self.assertEqual(mconcat(arr, mempty([])), mconcat(mempty([]), arr))

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_associativity(self, arr1: List[T], arr2: List[T], arr3: List[T]) -> None:
        a = from_list(arr1)
        b = from_list(arr2)
        c = from_list(arr3)
        self.assertEqual(mconcat(mconcat(a, b), c), mconcat(a, mconcat(b, c)))

    def test_api(self) -> None:
        empty: List[int] = []
        l1 = cons(cons(empty, None), 1)
        l2 = cons(cons(empty, 1), 2)
        l3 = cons(cons(empty, 2), 1)
        # TODO: conj to add elements to the end
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[1]")
        self.assertEqual(str(l2), "[1, 2]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(empty, None), 1))
        self.assertEqual(length(empty), 0)
        self.assertEqual(length(l1), 1)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, 0)), "[1]")
        self.assertEqual(str(remove(l1, 1)), "[]")
        self.assertFalse(member(empty, 0))
        self.assertFalse(member(l1, 0))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(l2, reverse(l3))
        self.assertEqual(to_list(l1), [1])
        self.assertEqual(l2, from_list([1, 2]))
        self.assertEqual(mconcat(l2, l3), from_list([1, 2, 2, 1]))
        self.assertEqual(filter_func(l2, is_odd), [1])
        self.assertNotEqual(filter_func(l2, is_even), [1])
        self.assertEqual(map_func(l2, square), [1, 4])
        self.assertEqual(reduce_func(l2, sum), 3)
        self.assertEqual(mempty(l2), [])
        buf = []
        for e in l2:
            buf.append(e)
        self.assertEqual(buf, [1, 2])
        lst = to_list(l2) + to_list(l3)
        for e in l2:
            lst.remove(e)
        for e in l3:
            lst.remove(e)
        self.assertEqual(lst, [])
