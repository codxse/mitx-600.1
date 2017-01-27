#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:00:00 2017

@author: Nadiar
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while (b != 0):
        iter = b
        b = a % b
        a = iter
    return a
    
print(
    gcdIter(2, 12) == 2,
    
    gcdIter(6, 12) == 6,
    
    gcdIter(9, 12) == 3,
    
    gcdIter(17, 12) == 1)