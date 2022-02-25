# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:15:01 2021

@author: SC
"""

a = 0.1
b = 0.2
expected = 0.3
computed = a+b
correct = expected==computed 
print(correct)
print('%.17f,%.17f,%.17f,%.17f'%(a,b,expected,computed))