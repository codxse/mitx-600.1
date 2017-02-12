#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:38:38 2017

@author: Nadiar
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    if len(listA) == 0:
        return 0
    else:
        return listA[0] * listB[0] + dotProduct(listA[1:], listB[1:])