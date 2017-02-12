#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:26:38 2017

@author: Nadiar
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    
    while True:
        if num - base**exp < 0:
            temp = exp
            exp -= 1 
            mmap = {}
            mmap[abs(num-base**exp)] = exp
            mmap[abs(num-base**temp)] = temp
            flor = min(mmap.keys())
            if len(mmap) == 1:
                return mmap[flor] - 1
            else:
                return mmap[flor]
        elif num - base**exp == 0:
            return exp
        else:
            exp += 1
    
print(closest_power(3,12)) #2
print(closest_power(4,12)) #2
print(closest_power(4,1)) #0
print(closest_power(2, 192)) #7
print(closest_power(5, 375.0)) #3
print(closest_power(10, 550.0)) #2