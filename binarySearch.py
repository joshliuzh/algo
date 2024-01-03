#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 15:45:57 2021

@author: Josh Liu
"""

def searchRight(nums, target):
    """
    Binary search that returns the minimum index i, such that A[i] >= target. If no such element exists, including if nums is empty, return N, the length of A.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    Equivalent to bisect.bisect_left
    """
    if not nums:
        return 0
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
   
# let's try some examples:
A = [0, 4, 4, 9, 16]
print(searchRight(A, -1)) # returns 0
print(searchRight(A, 0)) # returns 0
print(searchRight(A, 1)) # returns 1
print(searchRight(A, 4)) # returns 1
print(searchRight(A, 8)) # returns 3
print(searchRight(A, 9)) # returns 3
print(searchRight(A, 16)) # returns 4
print(searchRight(A, 20)) # returns 5

def searchLeft(nums, target):
    """
    Binary search that returns the maximum index i, such that A[i] <= target. If no such element exists, including if nums is empty, return -1.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    Equivalent to bisect.bisect_right
    """
    if not nums:
        return -1
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi
    
# let's try some examples:
A = [0, 4, 4, 9, 16]
print(searchLeft(A, -1)) # returns -1
print(searchLeft(A, 0)) # returns 0
print(searchLeft(A, 1)) # returns 0
print(searchLeft(A, 4)) # returns 2
print(searchLeft(A, 8)) # returns 2
print(searchLeft(A, 9)) # returns 3
print(searchLeft(A, 16)) # returns 4




