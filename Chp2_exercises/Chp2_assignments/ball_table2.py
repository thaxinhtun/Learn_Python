# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:25:11 2021

@author: SC
"""

#exercise 2.8

v0 = 5
g = 9.81
b = 2*v0/g
n = 10
a = 0
h = (b-a)/n

t = [ a+i*h for i in range(0,n+1)]
y = [v0*t[i]-0.5*g*t[i]**2 for i in range (0,n+1)]
print ("t        ","y")
for t1,t2 in zip(t,y):
    print("%5.2f  %5.2f"%(t1,t2))
