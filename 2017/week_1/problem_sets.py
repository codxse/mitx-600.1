#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:46:49 2017

@author: Nadiar
"""

# problem 1

s = "azcbobobegghakl"
vowels = "aiueo"
nVowel = 0

for c in s:
    if c in vowels:
        nVowel += 1
        
print("Number of vowels:", nVowel)

# problem 2

s = 'azcbobobegghakl'
nBob = 0

for i in range(len(s)):
    if i <= len(s)-3:
        if s[i:i+3] == "bob":
            nBob += 1
    
print("Number of times bob occurs is:", nBob)

# problem 3

s = 'azcbobobegghakl'
longestStr = ""

for i in range(0, len(s)-1):
    tempStr = s[i]
    
    while s[i] <= s[i+1]:
        if s[i] == s[len(s)-2]:
            tempStr += s[i+1]
            break
        
        tempStr += s[i+1]
        i += 1
    
    if len(tempStr) > len(longestStr):
        longestStr = tempStr

print("Longest substring in alphabetical order is:", longestStr)