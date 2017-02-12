#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:52:40 2017

@author: Nadiar
"""
def f(a,b):
    return a + b

def union(l1,l2):
    temp = []
    if len(l1) > len(l2):
        for l in l2:
            if l in l1:
                temp.append(l)
    else:
        for l in l1:
            if l in l2:
                temp.append(l)
    return temp

def difference(l1,l2):
    uni = union(l1,l2)
    l3 = l1 + l2
    temp = []
    for l in l3:
        if l not in uni:
            temp.append(l)
            
    # get unique
    return list(set(temp))
        
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    dif = difference(list(d1.keys()), list(d2.keys()))
    uni = union(list(d1.keys()), list(d2.keys()))   
    difMap = {}
    uniMap = {}
    for k in uni:
        uniMap[k] = f(d1[k], d2[k])
    for k in dif:
        try:
            difMap[k] = d1[k]
        except KeyError:
            difMap[k] = d2[k]
    
    return (uniMap, difMap)        


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2))
#({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}))