# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:46:08 2021

@author: SC
"""

#exercise 2.15

F = [i for i in range(0,100,10)]
C = [ (5.0/9 )*(F[i]-32) for i in range(len(F))]
Capprox= [0.5*(F[i]-32) for i in range(len(F))]
ans = [[F1,C1,Ca1]for F1,C1,Ca1 in zip(F,C,Capprox)]
print('F     ','C   ','Capprox ' )
for F1,C1,Ca1 in ans:
    print("%6.2f %6.2f %6.2f"%(F1,C1,Ca1))
    