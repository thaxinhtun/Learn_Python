# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:58:10 2021

@author: SC
"""

#exercise2.16

v0 = 5
g = 9.81
b = 2*v0/g
n = 10
a = 0
h = (b-a)/n

t = [ a+i*h for i in range(0,n+1)]
y = [v0*t[i]-0.5*g*t[i]**2 for i in range (0,n+1)]

ty1 = [t,y]  #list of table columns
print ("t        ","y")
for i in range(len(t)):
    print("%5.2f  %5.2f"%(ty1[0][i],ty1[1][i]))
    
ty2 = [[t1,y1] for t1,y1 in zip(t,y)] #list of table rows
print ("t        ","y")
for t1,y1 in ty2:
    print("%5.2f  %5.2f"%(t1,y1))
