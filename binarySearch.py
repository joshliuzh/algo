#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 15:45:57 2021

@author: Josh Liu
"""



def searchLeft(nums, target):
    """
    Binary search that returns the maximum index i, such that A[i] <= target. If no such element exists, return -1.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    """
    
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi
    


# Again, let's try some examples:
A = [0, 1, 1, 2]
searchLeft(A, -1) # returns -1
searchLeft(A, 0) # returns 0
searchLeft(A, .5) # returns 0
searchLeft(A, 1) # returns 2
searchLeft(A, 1.5) # returns 2
searchLeft(A, 2) # returns 3
searchLeft(A, 2.1) # returns 3


def searchRight(nums, target):
    """
    Binary search that returns the minimum index i, such that A[i] >= target. If no such element exists, return N, the length of A.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo



# Now let's try some examples:
A = [0, 1, 1, 2]
searchRight(A, -1) # returns 0
searchRight(A, 0) # returns 0
searchRight(A, .5) # returns 1
searchRight(A, 1) # returns 1
searchRight(A, 1.5) # returns 3
searchRight(A, 2) # returns 3
searchRight(A, 2.1) # returns 4

