#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 15:31:15 2017

@author: Nadiar
"""

# 1

a = 2

while (a <= 10):
    print(a)
    a += 2

print("Goodbye!")

# 2

print("Hello!")

a = 10

while(a >= 2):
    print(a)
    a -= 2
    
# 3

temp = 0
inc = 1
end = 21

while (end >= inc):
    temp += inc
    inc += 1
    
print(temp)