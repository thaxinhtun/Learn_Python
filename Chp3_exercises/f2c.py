# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:54:17 2021

@author: SC
"""

def C(F):
    return 5/9*(F-32)

def F(C):
    return 9/5*C +32

tol = 1E-14
c=0
if ( C(F(c)) - c <tol):
    print(C(F(c)),c)
    print("test pass")
else:
    print("test fail")