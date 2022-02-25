# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:35:17 2021

@author: SC
"""

#exercise 2.14

q = [['a','b','c'],['d','e','f'],['g','h']]

#(a)
print(q[0][0])
print(q[1])
print(q[2][-1])
print(q[1][0])
print(q[-1][-2])
print("\n")

#(b)
for i in q:
    for j in range(len(i)):
        print(i[j])
