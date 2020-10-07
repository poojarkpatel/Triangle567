"""
The program has three different functions to calculate
vowels, checks the last occurence in string, check 
if the my_enumerate function emulates the python's 
build in function enumerate()
"""
from typing import Optional, Sequence, Iterator

def count_vowels(s: str) -> int:
    """ returns the number of vowels in the string s """
    count: int = 0
    inputString: str = s.lower()
    for i in range (len(inputString)):
        if inputString[i] in ['a','e','i','o','u']:
            count += 1
    return count

def last_occurrence(target: any, sequence: Sequence[any]) -> Optional[int]:
    """ returns the offset from 0 of the last occurrence of target in seq """
    targetList: any = []
    for offset, s in enumerate(sequence):
        if s == target:
            targetList.append(offset)
    print(f"len {len(targetList)}")
    lastOccurrence: int = len(targetList) - 1
    if len(targetList)!= 0:
        return targetList[lastOccurrence]
    else:
        return None

def my(seq: Sequence[any]) -> Iterator[any] :
    """ emulates the behavior of Python's built in enumerate() function.        
    For each call, return a tuple with the offset from 0 and the next item """   
    for i in range(len(seq)):
         yield i, seq[i]

def my_enumerate(seq: Sequence[any]) -> Iterator[any] :
    """ emulates the behavior of Python's built in enumerate() function.        
    For each call, return a tuple with the offset from 0 and the next item """ 
    List1:list = []
    for i in my(seq):
        List1.append(i)
    return List1
