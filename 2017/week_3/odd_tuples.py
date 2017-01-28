#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:11:15 2017

@author: Nadiar
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    if (len(aTup) == 0):
        return ()
    else:
        return aTup[0:1] + oddTuples(aTup[2:])
