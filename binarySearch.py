#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 15:45:57 2021

@author: Josh Liu
"""

def binSearch1(A, t): 
    """
    Binary search that returns the minimum index i, such that A[i] >= target. If no such element exists, return N, the length of A.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    """
    
    
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2 # difference (1)
        if A[m] >= t:
            r = m
        else:
            l = m + 1
    return l


# Now let's try some examples:
A = [0, 1, 1, 2]
binSearch1(A, -1) # returns 0
binSearch1(A, 0) # returns 0
binSearch1(A, .5) # returns 1
binSearch1(A, 1) # returns 1
binSearch1(A, 1.5) # returns 3
binSearch1(A, 2) # returns 3
binSearch1(A, 2.1) # returns 4

def binSearch2(A, t):
    """
    Binary search that returns the maximum index i, such that A[i] <= target. If no such element exists, return -1.
    Input: A, a list of elements to be searched. MUST BE sorted in ascending order.
            t: target;
            
    Returns: an integer
    """
    
  
    l, r = -1, len(A) - 1
    while l < r:
        m = (l + r) // 2 + (l + r) % 2 # difference (1)
        if A[m] <= t:
            l = m
        else:
            r = m - 1
    return r

# Again, let's try some examples:
A = [0, 1, 1, 2]
binSearch2(A, -1) # returns -1
binSearch2(A, 0) # returns 0
binSearch2(A, .5) # returns 0
binSearch2(A, 1) # returns 2
binSearch2(A, 1.5) # returns 2
binSearch2(A, 2) # returns 3
binSearch2(A, 2.1) # returns 3
