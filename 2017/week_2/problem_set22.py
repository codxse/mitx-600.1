#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:41:11 2017

@author: Nadiar
"""

balance = 4773
annualInterestRate = 0.2

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month =
    (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

monthlyInterestRate = annualInterestRate / 12.0
    
def main(minimumFixedMonthlyPayment):
    
    def monthlyUnpaidBalance(balance):
        return balance - minimumFixedMonthlyPayment

    def updatedBalanceEachMonth(balance):
        return monthlyUnpaidBalance(balance) + monthlyInterestRate * monthlyUnpaidBalance(balance)
        
    def loop(balance, nMonth):
        if (nMonth < 1):
            return balance
        else:
            return loop(updatedBalanceEachMonth(balance), nMonth-1)
            
    def isPaid(balance):
        return loop(balance, 12) <= 0

    if isPaid(balance):
        return minimumFixedMonthlyPayment
    else:
        return main(minimumFixedMonthlyPayment + 10)
        
print("Lowest Payment:", main(10))
        
