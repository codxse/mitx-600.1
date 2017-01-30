#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:39:10 2017

@author: Nadiar
"""

#secretWord = 'durian'
#lettersGuessed =  []

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''   
    
    if len(lettersGuessed) == 1:
        return lettersGuessed[0] in secretWord
    
    if len(lettersGuessed) == 0:
        return False
            
    if lettersGuessed[0] in secretWord:
        return True and isWordGuessed(secretWord, lettersGuessed[1:])
    else:
        return isWordGuessed(secretWord, lettersGuessed[1:])
    
    
    
#print(isWordGuessed(secretWord, lettersGuessed))

