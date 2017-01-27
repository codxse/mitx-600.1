#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:53:59 2017

@author: Nadiar
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

"""
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month =
    (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

monthlyInterestRate = annualInterestRate / 12.0

def minimumMonthlyPayment(balance):
    return monthlyPaymentRate * balance

def monthlyUnpaidBalance(balance):
    return balance - minimumMonthlyPayment(balance)
    
def updatedBalanceEachMonth(balance):
    return monthlyUnpaidBalance(balance) + monthlyInterestRate * monthlyUnpaidBalance(balance)
    
def loop(balance, nMonth):
    if (nMonth <= 1):
        return updatedBalanceEachMonth(balance)
    else:
        return loop(updatedBalanceEachMonth(balance), (nMonth-1))
        
def main(balance):
    return loop(balance, 12)
    
print("Remaining balance: %.2f" %main(balance))
                