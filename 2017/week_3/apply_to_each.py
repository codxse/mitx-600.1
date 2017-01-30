#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:41:10 2017

@author: Nadiar
"""

testList = [1, -4, 8, -9]

def abs(x):
    if (x >= 0):
        return x
    else:
        return -x

def halve(a):
    return a/2
        
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

# [2, -3, 9, -8]
def inc(a):
    return a+1

# [1, 16, 64, 81]
def square(a):
    return a*a
