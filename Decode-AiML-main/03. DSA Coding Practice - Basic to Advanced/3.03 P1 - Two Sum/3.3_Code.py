# -*- coding: utf-8 -*-
"""3.3_code.ipynb

# P1: Two-Sum

Problem : Two Sum
Given arr, an array of numbers and Target
Find [i1,i2]

Constraints:
2 <= arr <= 10^4

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

print(twoSum([5,2,4,11,13],17)) # [2,4]
print(twoSum([5,2,4,11,13],23)) # []

"""### Approach 2. Hashing"""

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

print(twoSum([5,2,4,11,13],17)) # [2,4]
print(twoSum([5,2,4,11,13],23)) # []

"""Practice Link : https://leetcode.com/problems/two-sum/description/"""