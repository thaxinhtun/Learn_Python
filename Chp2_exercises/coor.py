# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:24:22 2021

@author: SC
"""

#exercise 2.6

a = 0
b = 1
n = 4
h = (b-a)/n
#(a)
xlist = []
for i in range(n+1):
    xlist.append(a + i*h)
print(xlist )

#(b)list comprehension
xlist2 = [a + h*i for i in range(n+1)]
print(xlist2)