# -*- coding: utf-8 -*-
"""3.4_code.ipynb

# P2: Two Sum II - Input Array Is Sorted

Problem : Two Sum II - Input Array Is Sorted
Given arr, a sorted array of numbers and Target
Find [i1,i2]

### Approach 1. Brute-Force
"""

from typing import List

"""
To be Implemented
"""
def twoSum(arr: List[int], Target: int) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == Target:
                return [i,j]

    return []

print(twoSum([2,4,5,11,13],17)) # [1,4]
print(twoSum([2,4,5,11,13],23)) # []

"""## Approach 2. Hashing"""

"""
To be Implemented
"""
def twoSum(arr: List[int], Target: int) -> List[int]:
    hashDict = {} # value,index
    n = len(arr)

    for i in range(n): # arr[i]
        if Target - arr[i] in hashDict:
            return [i, hashDict[Target - arr[i]]]
        hashDict[arr[i]] = i

    return []

print(twoSum([2,4,5,11,13],17)) # [1,4]
print(twoSum([2,4,5,11,13],23)) # []

"""### Approach 3. Two Pointers"""

"""
To be Implemented => O(n), O(1)
"""
def twoSum(arr: List[int], Target: int) -> List[int]:
    l, r = 0, len(arr)-1
    while l<r: # 2-pointer
        if arr[l]+arr[r] == Target:
            return [l,r]

        elif arr[l]+arr[r] < Target:
            l += 1

        else:
            r -= 1
    return []

print(twoSum([2,4,5,11,13],17)) # [1,4]
print(twoSum([2,4,5,11,13],23)) # []

"""Practice Link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/"""