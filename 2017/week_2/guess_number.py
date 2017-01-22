#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:03:04 2017

@author: Nadiar
"""

max_ = 100
min_ = 0
guess = max_/2
input_ = ""

print("Please think of a number between 0 and 100!")

while input_ != "c":
    print("Is your secret number " + str(int(guess)) + "?")
    input_ = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
     
    if input_ == "h":
        max_ = guess
        guess = (max_ + min_) // 2
        
    if input_ == "l":
        min_ = guess
        guess = (max_ + min_) // 2
        
    if input_ not in "hlc":
        print("Sorry, I did not understand your input.")
        
        
print("Game over. Your secret number was:",str(int(guess)))


# recursive

def guess_number(guess, h=100, l=0):
    print("Is your secret number " + str((h+l)//2) + "?")
    input_ = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if input_ == "c":
        print("Game over. Your secret number was:",str(int(guess)))
    elif input_ == "h":
        guess_number((h+l)//2, (h+l)//2, l)
    elif input_ == "l":
        guess_number((h+l)//2, h, (h+l)//2)
    else:
        print("Sorry, I did not understand your input.")
        guess_number(guess, h, l)
        
print("Please think of a number between 0 and 100!")
guess_number(50)
        
    