# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:18:54 2021

@author: SC
"""

initial_amount = 100
p = 5 # interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount += p/100*amount
    years += 1
print( years)