
# GROUP-watermelon - lab 2 - variant 2

This is a code of Dynamic array in immutable style
(interaction with the object cannot change it).
The reason for such data structure design is: more relevant for multi-thread programming.
Some algorithms and data structures are simple to implement in this way
(especially structure with recursive data structure).

## Project structure

- `dynamicArray.py` -- Definition of dynamic array structure method.
  It includes the methods to realize the functions of lab2.
- `dynamicArray_test.py` -- unit, PBT tests and API test for `dynamicArray`.

## Features

- PBT: test_from_list_to_list, test_len_size, test_monoid_identity, test_monoid_associativity

## Contribution

- Gu Haoqin (212320036@hdu.edu.cn) -- Method compilation.
- Liu Huasheng (peanut2021@hdu.edu.cn) -- Method test

## Changelog

- 10.06.2022 - 1
  - Update code (Check immutability by property-based testing).
- 10.06.2022 - 0
  - Update code (Add type hints).
- 01.06.2022 - 0
  - Update code (implement and test).
- 16.05.2022 - 2
  - Add code (implement and test).
- 16.05.2022 - 1
  - Update README. Add formal sections.
- 16.05.2022 - 0
  - Initial.

## Design notes

- Compare mutable and immutable implementation
  - The mutable implementation performs all the changes by changing
    the initial structure, which can cause errors when sharing variables.
    The immutable implementation builds a new structure without changing
    the initial variable values. The immutable data structure allows a developer
    to work with data safely from many places and processes without any surprises
    with broken states or unexpected data changes.
- Implementation restrictions
  - If you want to add None value, you need to use str type,
    otherwise the program will treat it as empty.
- Possible implementation errors
  - If the elements in the array are of type str, using the reduce function
    on the array will not achieve the function of adding, but concatenate
    the str elements together.
