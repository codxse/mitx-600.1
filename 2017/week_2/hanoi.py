#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:52:44 2017

@author: Nadiar
"""

def printMove(from_, to_):
    print('move from ' + str(from_) + ' to ' + str(to_))

def towers(n, from_, to_, spare):
    if (n == 1):
        printMove(from_, to_)
    else:
        towers(n-1, from_, spare, to_)
        towers(1, from_, to_, spare)
        towers(n-1, spare, to_, from_)