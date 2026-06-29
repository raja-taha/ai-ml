# -*- coding: utf-8 -*-
"""3.6_code.ipynb

# P4: 4Sum

Problem : 4Sum
Given arr, an array of numbers and Target
Find list of quadruplets  - [arr[i],arr[j],arr[k],arr[l]] such that their sum is equal to Target
and i,j,k and l are distinct
duplicates not allowed in ans

### Approach 1. Brute-Force
"""

from typing import List

"""
To be Implemented
"""
def fourSum(arr: List[int], Target: int) -> List[int]:
    n = len(arr)
    ans = set() # hashing
    #iterate and find all possible quads
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == Target:
                        ans.add(tuple(sorted([arr[i], arr[j], arr[k], arr[l]])))

    return list(ans)

# Time Complexity - O(n^4)
# Space Complexity - O(n^4)

print(fourSum([1,0,-1,0,-2,2],1)) # [(-2, 0, 1, 2), (-1, 0, 0, 2)]
print(fourSum([2,2,2,4,2], 10)) # [(2, 2, 2, 4)]

"""### Approach 2. Better - Sorting + 2-Pointers + Set"""

"""
To be Implemented
"""
def fourSum(arr: List[int], Target: int) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    ans = set()

    # main code logic begins
    # use 2 loops for i and j
    for i in range(n):
        for j in range(i+1,n):
            # 2-pointer code for 2sum program - arr is sorted
            target = Target - (arr[i] + arr[j])
            left = j+1
            right = n-1

            while left<right:
                if (arr[left]+arr[right]> target):
                    right -=1
                elif (arr[left]+arr[right]< target):
                    left +=1
                else: # sum == target
                    ans.add(tuple([arr[i],arr[j],arr[left],arr[right]])) # adding to a set
                    left +=1
                    right -=1

    return list(ans)


# Time Complexity - O(n^3)
# Space Complexity - O(n^4)

print(fourSum([1,0,-1,0,-2,2],1)) # [(-2, 0, 1, 2), (-1, 0, 0, 2)]
print(fourSum([2,2,2,4,2], 10)) # [(2, 2, 2, 4)]

"""### Approach 3. Optimal - Sorting + 2-Pointers"""

"""
To be Implemented
"""
def fourSum(arr: List[int], Target: int) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    ans = []

    # main code logic begins
    # use 2 loops for i and j
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue

            # 2-pointer code for 2sum program - arr is sorted
            target = Target - (arr[i] + arr[j])
            left = j+1
            right = n-1

            while left<right:
                if (arr[left]+arr[right]> target):
                    right -=1
                elif (arr[left]+arr[right]< target):
                    left +=1
                else: # sum == target
                    t1 = arr[left]
                    t2 = arr[right]
                    ans.append(tuple([arr[i],arr[j],arr[left],arr[right]])) # adding to a set
                    while left<right and arr[left] == t1:
                        left+=1
                    while left<right and arr[right] == t2:
                        right -=1

    return ans


# Time Complexity - O(n^3)
# Space Complexity - O(n^4)

print(fourSum([1,0,-1,0,-2,2],1)) # [(-2, 0, 1, 2), (-1, 0, 0, 2)]
print(fourSum([2,2,2,4,2], 10)) # [(2, 2, 2, 4)]

"""Problem Link - https://leetcode.com/problems/4sum/description/"""