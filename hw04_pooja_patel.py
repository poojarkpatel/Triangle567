"""
The program has three different functions to calculate vowels,
checks the last occurence in string, check  if the
my_enumerate function emulates the python's build in function enumerate()
"""
from typing import Sequence, Iterator


def count_vowels(string: str) -> int:
    """ returns the number of vowels in the string s """
    count: int = 0
    input_string: str = string.lower()
    for value in enumerate(input_string):
        if value in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


def last_occurrence(target: any, sequence: Sequence[any]) -> int:
    """ returns the offset from 0 of the last occurrence of target in seq """
    target_list: any = []
    for offset, value in enumerate(sequence):
        if value == target:
            target_list.append(offset)
    last_occur: int = len(target_list) - 1
    # if len(target_list) != 0:
    return target_list[last_occur]


def my_enum(seq: Sequence[any]) -> Iterator[any]:
    """ emulates the behavior of Python's built in enumerate() function.
    For each call, return a tuple with the offset
    from 0 and the next item """
    for index, value in enumerate(seq):
        yield index, value


def my_enumerate(seq: Sequence[any]) -> Iterator[any] :
    """ emulates the behavior of Python's built in enumerate() function.
    For each call, return a tuple with the offset from 0 and the next item """
    list1: list = []
    for i in my_enum(seq):
        list1.append(i)
    return list1
