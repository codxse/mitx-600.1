#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 15:13:18 2017

@author: Nadiar
"""

varA = "hello"
varB = 1000

if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    
    elif varA == varB:
        print("equal")
    
    else:
        print("smaller")