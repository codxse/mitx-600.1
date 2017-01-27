#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:22:27 2017

@author: Nadiar
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    if (aStr == ''):
        return False
    if (len(aStr) == 1):
        return aStr == char
        
    temp = aStr[len(aStr) // 2]
    
    if (char == temp):
        return True
    elif (char < temp):
        return isIn(char, aStr[:(len(aStr) // 2)])
    else:
        return isIn(char, aStr[((len(aStr)//2)+1):])
