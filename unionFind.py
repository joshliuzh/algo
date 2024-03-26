#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:15:57 2021

@author: liuzhao
"""

parent = list(range(n))
rank = [0] * n

def find(x):
    nonlocal parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):

    nonlocal parent, rank

    xr, yr = find(x), find(y)
    if xr == yr:
        return
    rankx, ranky = rank[x], rank[y]
    if rankx < ranky:
        parent[xr] = yr

    else:
        parent[yr] = xr
        rank[xr] += rankx == ranky
        
