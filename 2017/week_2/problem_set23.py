#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 08:56:55 2017

@author: Nadiar
"""

balance = 320000
annualInterestRate = 0.2

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound =
    (Balance x (1 + Monthly interest rate)^12) / 12.0
"""

monthlyInterestRate = annualInterestRate / 12.0

def monthlyUnpaidBalance(balance, guess):
    return balance - guess

def updatedBalanceEachMonth(balance, guess):
    return monthlyUnpaidBalance(balance, guess) \
            + monthlyInterestRate * \
            + monthlyUnpaidBalance(balance, guess)
            
def updatedBalance(balance, guess, nMonth):
    """
    return balance after payment made with guess each month
    """
    if (nMonth < 1):
        return balance
    else:
        return updatedBalance(updatedBalanceEachMonth(balance, guess), guess, nMonth-1)

def remainingBalance(balance, guess):
    return updatedBalance(balance, guess, 12)

def monthlyPaymentLowerBound(balance):
    return balance / 12

def monthlyPaymentUpperBound(balance):
    return (balance * (1 + monthlyInterestRate)**12) / 12.0

def generateGuess(lower, upper):
    return (lower + upper) / 2
            
def bSearchIter(balance):
    lower = monthlyPaymentLowerBound(balance)    
    upper = monthlyPaymentUpperBound(balance)
    guess = (lower + upper) / 2
    debt = remainingBalance(balance, guess)
    
    # while guess is not minimum
    while not (debt <= 0.01 and debt >= -0.01):                
        # if we pay more
        if (debt < 0):
            upper = guess
            guess = (lower + upper) / 2
            debt = remainingBalance(balance, guess)
            # print("+++", debt)
        
        # if we pay less
        if (debt > 0):
            lower = guess
            guess = (lower + upper) / 2
            debt = remainingBalance(balance, generateGuess(lower, upper))
            # print("---", debt)         
            
    return guess

def bSearchRecur(balance, guess, lower, upper):
    if (remainingBalance(balance, guess) <= 0.01 and
        remainingBalance(balance, guess) >= -0.01):
        return guess
    if (remainingBalance(balance, guess) < 0):
        return bSearchRecur(balance, generateGuess(lower, guess), lower, guess)
    if (remainingBalance(balance, guess) > 0):
        return bSearchRecur(balance, generateGuess(guess, upper), guess, upper)
    
def main(balance):
    # return bSearchIter(balance)
    return bSearchRecur(balance,
                        generateGuess(monthlyPaymentLowerBound(balance),
                                      monthlyPaymentUpperBound(balance)),
                        monthlyPaymentLowerBound(balance),
                        monthlyPaymentUpperBound(balance))
                        
print("Lowest Payment: %.2f" %main(balance))
        
        