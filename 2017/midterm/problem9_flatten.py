#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:29:33 2017

@author: Nadiar
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if type(aList) != list:
        return [aList]
    elif aList == []:
        return []
    else:
        return flatten(aList[0]) + flatten(aList[1:])
    
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))