#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:32:52 2017

@author: Nadiar
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (b == 0):
        return a
    else:
        return gcdRecur(b, (a % b))
    
print(     
    gcdRecur(2, 12) == 2,
    gcdRecur(6, 12) == 6,
    gcdRecur(9, 12) == 3,
    gcdRecur(17, 12) == 1)