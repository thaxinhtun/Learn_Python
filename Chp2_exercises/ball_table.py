# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:38:05 2021

@author: SC
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:24:22 2021

@author: SC
"""

#exercise 2.7


v0 = 5
g = 9.81
b = 2*v0/g
n = 10
a = 0
h = (b-a)/n

#(a)
ylist = []
t = []
print("....................")
print('t      y(t) ')
print("********************")
for i in range(n+1):
    t.append(a+i*h)
    ylist.append(v0*t[i]-0.5*g*t[i]**2)
    print("%5.2f %5.2f" %(t[i],ylist[i] ))
    
import matplotlib.pyplot as plt
plt.plot(t,ylist)


#(b)list comprehension
#xlist2 = [a + h*i for i in range(n+1)]
#print(xlist2)