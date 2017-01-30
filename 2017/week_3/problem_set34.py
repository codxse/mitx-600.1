#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:48:29 2017

@author: Nadiar
"""
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

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord) == 1:
        if secretWord[0] in lettersGuessed:
            return secretWord[0]
        else:
            return "_ "
            
    if secretWord[0] in lettersGuessed:
        return secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
    else:
        return "_ " + getGuessedWord(secretWord[1:], lettersGuessed)
    
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

def hangIter(aMap):
    # Base Case
    if isWordGuessed(aMap['lettersGuessed'], aMap['secretWord']):
        print("Congratulations, you won!")
        
    elif aMap['nGuess'] > 0:
        print("You have " + str(aMap['nGuess']) + " guesses left.")
        print("Available letters: " + aMap['availableLetters'])
        char = input("Please guess a letter: ")
        aMap['nGuess'] -= 1
        
        if char in aMap['lettersGuessed']:
            print("Oops! You've already guessed that letter: " + 
                  str(aMap['displayLetterGuessed']))
            print("------------")
            hangIter(aMap)
        elif char in aMap['secretWord']:
            aMap['lettersGuessed'].append(char)
            aMap['displayLetterGuessed'] = getGuessedWord(aMap['secretWord'],
                                                          aMap['lettersGuessed'])
            aMap['availableLetters'] = getAvailableLetters(aMap['lettersGuessed'])
            
            print("Good guess: " + str(aMap['displayLetterGuessed']))
            print("------------")
            hangIter(aMap)
        else:
            aMap['lettersGuessed'].append(char)
            aMap['availableLetters'] = getAvailableLetters(aMap['lettersGuessed'])
            print("Oops! That letter is not in my word: " +
                  str(aMap['displayLetterGuessed']))
            print("------------")
            hangIter(aMap)
            
    # Base Case
    else:
        print("Sorry, you ran out of guesses. The word was " + 
              str(aMap['secretWord']) + ".")
        

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    aMap = {"secretWord": secretWord,
            "nGuess": 8, 
            "lettersGuessed": [],
            "displayLetterGuessed": "_",
            "availableLetters": "abcdefghijkmnopqrstuvwxyz"}
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    hangIter(aMap)
    
hangman("tahu")