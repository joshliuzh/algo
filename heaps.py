#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:40:14 2021

@author: liuzhao
"""

class minHeap:
    """
    Rudimentary min heap implemented with an array starting from index 0;
    In this way, a tree node with index i's left child is 2i+1, right child is 2i + 2;
    A node at index j has its parent node at index (j - 1) // 2.
    
    Also performs heapsort
    """
    def __init__(self):
        self.heap = []
        
    def push(self, val): # heapify up
        self.heap.append(val)
        n = len(self.heap)
        
        k = n - 1
        while k > 0 and self.heap[k] < self.heap[(k - 1) // 2]:
            #print(k)
            #print(self.heap)
            self.heap[k], self.heap[(k - 1) // 2] = self.heap[(k - 1) // 2], self.heap[k]
            k = (k - 1) // 2
        return True
    
    def pop(self):
        if not self.heap:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        to_be_returned = self.heap.pop()
        if self.heap: # heapify down
            #print(self.heap)
            n = len(self.heap)
            k = 0
            while (2 * k + 1 < n and self.heap[2 * k + 1] < self.heap[k]) or (2 * k + 2 < n and self.heap[2 * k + 2] < self.heap[k]):
                if 2 * k + 2 >= n or self.heap[2 * k + 1] < self.heap[2 * k + 2]: # only left child
                    self.heap[k], self.heap[2 * k + 1] = self.heap[2 * k + 1], self.heap[k]
                    k = 2 * k + 1
                else:
                    self.heap[k], self.heap[2 * k + 2] = self.heap[2 * k + 2], self.heap[k]
                    k = 2 * k + 2
                
        #print(self.heap)
        return to_be_returned
    
    def sort(self):
        out = []
        while self.heap:
            out.append(self.pop())
        self.heap = out
        return out
    
a = minHeap()
a.push(0)
a.push(1)
a.push(2)
a.push(3)
a.push(-1)
a.push(-9)
a.pop()
a.pop()

b = minHeap()
for i in range(0, 50):
    b.push(i)

b_sorted = b.sort()
print(b_sorted)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
