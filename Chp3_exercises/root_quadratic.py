# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:16:40 2021

@author: SC
"""

from math import *

def roots(a,b,c):
    root = b**2 - 4*a*c
    sqr_root = sqrt(root)
    sol1 = (-b + sqr_root) /( 2*a)
    sol2  =(-b - sqr_root) /( 2*a)
    return sol1, sol2


def test_roots_float():
     expected_1 =  -0.2
     expected_2 = -1.0
     ans = 5*(expected_1**2)+6*expected_1+1
     success = ans == 0
     msg = 'expected != computed'
     if success == True:
         print("pass")
         print(type(expected_1()))
     else:
        print("fail")
     assert success,msg
     
test_roots_float()
print(roots(5,6,1))    