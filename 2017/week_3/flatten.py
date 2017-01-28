#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:53:06 2017

@author: Nadiar
"""
def flatten(aList):
    
    # if empty list
    if (aList == []):
        return []
    
    # if not list
    if (type(aList) is not list):
        return [aList]
    
    # if aList is list type
    if (type(aList) is list):
        return flatten(aList[0]) + flatten(aList[1:])

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    return len(flatten(list(aDict.values())))