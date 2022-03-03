# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:05:20 2021

@author: SC
"""

from math import sqrt,exp,pi

def guass(x,m=0,s=1):
    return (1/sqrt(2*pi)*s)* exp(-0.5 * ((x-m)/s)**2)

m=0;s=1

xmin = m-(5*s)
xmax = m+(5*s)
n=10
h = (xmax-xmin)/n
x=[xmin + i*h for i in range (1,n+1)]
for e in x:
    print("x=%5.3f f(x)=%5.3f"%(e,guass(e)))