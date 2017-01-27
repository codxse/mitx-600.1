#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:07:09 2017

@author: Nadiar
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    res = 1
    for i in range(1,(exp + 1)):
        res *= base
    
    return res
