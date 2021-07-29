#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:45:50 2021

@author: liuzhao
"""
import collections
def lengthOfLongestSubstringKDistinct(arr, k) -> int:
"""
Using sliding window, return the length of the longest subarray with at most k distinct elements.
"""
    if k == 0:
        return 0
    l, r = 0, 0
    out = 0
    mapping = collections.defaultdict(int)
        
    while r < len(arr):
        mapping[arr[r]] += 1
        r += 1
        while len(mapping) > k:
            mapping[arr[l]] -= 1
            if mapping[arr[l]] == 0:
                del mapping[arr[l]]
            l += 1
        out = max(out, r - l)
    return out
                

def countOfSubstringsWithAtMostKDistinct(arr, k) -> int:
"""
Using sliding window, return the number of the subarrays with at most k distinct elements.
"""    
    if k == 0:
        return 0
    l, r = 0, 0
    out = 0
    mapping = collections.defaultdict(int)
        
    while r < len(arr):
        mapping[arr[r]] += 1
        r += 1
        while len(mapping) > k:
            mapping[arr[l]] -= 1
            if mapping[arr[l]] == 0:
                del mapping[arr[l]]
            l += 1
        out  += r - l
    return out
A = [0, 1, 2, 3, 4, 5, 6]
countOfSubstringsWithAtMostKDistinct(A, 3)
