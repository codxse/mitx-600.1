#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:06:58 2017

@author: Nadiar
"""

def drop(char, alphabet):
    if char in alphabet:
        return alphabet.split(char)[0] + alphabet.split(char)[1]
    else:
        return alphabet

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    temp = "abcdefghijklmnopqrstuvwxyz"
    
    for c in lettersGuessed:
        temp = drop(c, temp)
            
    return temp        
    
    
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz