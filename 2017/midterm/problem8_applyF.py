#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:21:48 2017

@author: Nadiar
"""
def f(i):
    return i + 2

def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    if L != []:
        temp = []
        for i in L:
            if (g(f(i))):
                temp.append(i)
        L.clear()
        
        # mutate            
        for x in temp:
            L.append(x) 
            
        if(L):
            return max(L)
    
    return -1
    
L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)