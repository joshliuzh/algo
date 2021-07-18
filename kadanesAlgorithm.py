#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:34:28 2021

@author: liuzhao
"""

def kadane(A):
    """
    Return the starting and ending index of a subarray i, j, such that sum(A[i, j]) is maximized.
    Input: a list of numbers;
    Returns, a tuple containing 2 integers
    """
    
    n = len(A)
    if not A:
        return -1, -1
    starting, ending = 0, 1
    curr_start = 0, 1
    globalMax = A[0]
    currMax   = A[0]
    for i in range(1, n):
        #print(A[i])
        if currMax < 0:
            curr_start = i    
        currMax = max(A[i], currMax + A[i])
        
        if currMax > globalMax:
            starting = curr_start
            ending = i + 1
        globalMax = max(currMax, globalMax)
        #print(globalMax)
    print(starting, ending)
    return starting, ending, globalMax

A = [-1, 1, -1, 3]
B = [1, -2, 4, -8, 16, -32, 64]
kadane(A) # returns 3, 4, 4
kadane(B) # returns 6, 7, 64
