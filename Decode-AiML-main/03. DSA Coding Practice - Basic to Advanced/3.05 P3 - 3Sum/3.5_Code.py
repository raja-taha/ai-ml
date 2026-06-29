# -*- coding: utf-8 -*-
"""3.5_code.ipynb

# P3: 3Sum

Problem : 3Sum
Given arr, an array of numbers
Find list of triplets - [arr[i],arr[j],arr[k]] and i,j and k are distinct
duplicates not allowed in ans

### Approach 1. Brute-Force
"""

from typing import List

"""
To be Implemented
"""
def threeSum(arr: List[int]) -> List[int]:
    ans = set() #hashing
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    ans.add(tuple(sorted([arr[i],arr[j],arr[k]])))
    return list(ans)

print(threeSum([-5,2,4,3,1,1,4,1])) # [(-5, 1, 4), (-5, 2, 3)]
print(threeSum([2,1,1,-1,-1,0,0,-1,0])) # [[-1, -1, 2], [-1, 0, 1], [0, 0, 0]]

"""### Approach 2. Better - Sorting + 2 Pointers + Set"""

"""
To be Implemented
"""
def threeSum(arr: List[int]) -> List[List[int]]:
    arr.sort() # inplace
    n = len(arr)
    ans  = set()
    for i in range(n): # i+1, n-1

        # 2 pointer approach - for 2 sum
        left = i+1
        right = n-1
        target = -1*arr[i]
        while left<right:
            if arr[left]+arr[right] > target:
                right -=1
            elif arr[left]+arr[right] < target:
                left += 1
            else: # triplet milta hai
                t1, t2 = arr[left], arr[right]
                ans.add(tuple([arr[i],arr[left],arr[right]]))
                left += 1
                right -=1

    return ans

# Time Complexity - O(n^2)
# Space Complexity - O(n^3)

print(threeSum([-5,2,4,3,1,1,4,1])) # [(-5, 1, 4), (-5, 2, 3)]
print(threeSum([2,1,1,-1,-1,0,0,-1,0])) # [[-1, -1, 2], [-1, 0, 1], [0, 0, 0]]



"""### Approach 3. Optimal - Sorting + 2 Pointers"""

"""
To be Implemented
"""
def threeSum(arr: List[int]) -> List[List[int]]:
    arr.sort() # inplace
    n = len(arr)
    ans  = []
    for i in range(n): # i+1, n-1
        if i>0 and arr[i] == arr[i-1]:
            continue
        # 2 pointer approach - for 2 sum
        left = i+1
        right = n-1
        target = -1*arr[i]
        while left<right:
            if arr[left]+arr[right] > target:
                right -=1
            elif arr[left]+arr[right] < target:
                left += 1
            else: # triplet milta hai
                t1, t2 = arr[left], arr[right]
                ans.append([arr[i],arr[left],arr[right]])
                while left<right and arr[left] == t1:
                    left += 1
                while left<right and arr[right] == t2:
                    right -=1

    return ans



# Time Complexity - O(n^2)
# Space Complexity - O(n^3)

print(threeSum([-5,2,4,3,1,1,4,1])) # [(-5, 1, 4), (-5, 2, 3)]
print(threeSum([2,1,1,-1,-1,0,0,-1,0])) # [[-1, -1, 2], [-1, 0, 1], [0, 0, 0]]

"""Practice Link - https://leetcode.com/problems/3sum/description/"""