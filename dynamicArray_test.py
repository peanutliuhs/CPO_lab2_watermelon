import unittest
from dynamicArray import *
from hypothesis import given
import hypothesis.strategies as st
from typing import List


class TestDynamicArray(unittest.TestCase):

    def test_cons(self) -> None:
        arr = DynamicArray()
        self.assertEqual(cons(arr, 1)._values, [1])
        self.assertEqual(cons(cons(arr, 1), 4)._values, [1, 4])

    def test_remove(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(remove(arr, 1)._values, [4, 5, 3])
        self.assertEqual(remove(remove(arr, 1), 3)._values, [4, 5])

    def test_length(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(length(arr), 4)

    def test_member(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(member(arr, -1), False)
        self.assertEqual(member(arr, 5), True)

    def test_reverse(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(reverse(arr)._values, [3, 5, 4, 1])

    def test_from_list(self) -> None:
        lst = [1, 4, 5, 3]
        self.assertEqual(from_list([1, 4, 5, 3])._values, [1, 4, 5, 3])

    def test_to_list(self) -> None:
        arr1 = DynamicArray()
        self.assertEqual(to_list(arr1), [])
        arr2 = DynamicArray(1, 4, 5, 3)
        self.assertEqual(to_list(arr2), [1, 4, 5, 3])

    def test_find(self) -> None:
        arr1 = DynamicArray()
        self.assertEqual(value_find_key(arr1, 0), -1)
        self.assertEqual(value_find_key(arr1, 1), -1)
        arr2 = DynamicArray(1, 4, 5, 3)
        self.assertEqual(value_find_key(arr2, 5), 2)
        self.assertEqual(key_find_value(arr2, 1), 4)

    def test_ﬁlter(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(filter_func(arr, is_odd)._values, [1, 5, 3])
        self.assertEqual(filter_func(arr, is_even)._values, [4])

    def test_map(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(map_func(arr, square)._values, [1, 16, 25, 9])

    def test_reduce(self) -> None:
        arr = DynamicArray(1, 4, 5, 3)
        self.assertEqual(reduce_func(arr, sum), 13)

    def test_iter(self) -> None:
        arr1 = DynamicArray(1, 4, 5, 3)
        arr2 = DynamicArray(1, 4, 5, 3)
        get_next1 = iterator(arr1)
        get_next2 = iterator(arr2)
        self.assertEqual(get_next1(), 1)
        self.assertEqual(get_next2(), 1)
        self.assertEqual(get_next1(), 4)
        self.assertEqual(get_next2(), 4)
        self.assertEqual(get_next1(), get_next2())

    def test_mempty(self) -> None:
        arr1 = DynamicArray()
        self.assertEqual(mempty(arr1)._values, [])
        arr2 = DynamicArray(1, 4, 5, 3)
        self.assertEqual(mempty(arr2)._values, [])

    def test_mconcat(self) -> None:
        arr1 = DynamicArray()
        arr2 = DynamicArray(1, 4)
        arr3 = DynamicArray(5, 3)
        self.assertEqual(mconcat(arr1, arr1)._values, [])
        self.assertEqual(mconcat(arr1, arr2), arr2)
        self.assertEqual(mconcat(arr2, arr3), cons(
            cons(cons(cons(arr1, 1), 4), 5), 3))

    @given(st.lists(st.integers()))
    def test_from_list_to_list(self, lst: List[int]) -> None:
        arr = from_list(lst)
        tmp_lst = to_list(arr)
        self.assertEqual(lst, tmp_lst)

    @given(st.lists(st.integers()))
    def test_len_size(self, lst: List[int]) -> None:
        arr = from_list(lst)
        self.assertEqual(length(arr), len(lst))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst: List[int]) -> None:
        arr1 = DynamicArray()
        arr2 = from_list(lst)
        self.assertEqual(mconcat(mempty(arr1), arr2), arr2)
        self.assertEqual(mconcat(arr2, mempty(arr1)), arr2)
        self.assertEqual(mconcat(arr2, mempty(arr1)),
                         mconcat(mempty(arr1), arr2))

    @given(st.lists(st.integers()), st.lists(st.integers()),
           st.lists(st.integers()))
    def test_monoid_associativity(self, arr1: List[int],
                                  arr2: List[int], arr3: List[int]) -> None:
        a = from_list(arr1)
        b = from_list(arr2)
        c = from_list(arr3)
        self.assertEqual(mconcat(mconcat(a, b), c), mconcat(a, mconcat(b, c)))

    def test_api(self) -> None:
        empty = DynamicArray()
        l1 = cons(empty, 1)
        l2 = cons(cons(empty, 1), 2)
        l3 = cons(cons(empty, 2), 1)
        # TODO: conj to add elements to the end
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[1]")
        self.assertEqual(str(l2), "[1, 2]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(empty, 1))
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
        self.assertEqual(filter_func(l2, is_odd)._values, [1])
        self.assertNotEqual(filter_func(l2, is_even)._values, [1])
        self.assertEqual(map_func(l2, square)._values, [1, 4])
        self.assertEqual(reduce_func(l2, sum), 3)
        self.assertEqual(mempty(l2), empty)
        buf = []
        for e in l2._values:
            buf.append(e)
        self.assertEqual(buf, [1, 2])
        lst = to_list(l2) + to_list(l3)
        for e in l2._values:
            lst.remove(e)
        for e in l3._values:
            lst.remove(e)
        self.assertEqual(lst, [])
