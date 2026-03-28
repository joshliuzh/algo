#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:15:57 2021

@author: liuzhao
"""

class UnionFind:
    def __init__(self, n):
        # Initially, each element is its own parent
        self.parent = list(range(n))
        # Initially, each set has a size of 1
        self.size = [1] * n

    def find(self, x):
        # Path compression: make nodes point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by Size: attach the smaller tree to the larger tree
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True # Successfully merged
        return False # Already in the same set
