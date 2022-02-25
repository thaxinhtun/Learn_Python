# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:28:11 2021

@author: SC
"""

from math import *
x = 2*pi
r1 = sinh(x)
r2 = 0.5*exp(x) - exp(-x)
r3 = 0.5*(e**x - e**(-x))
print('%.16f,%.16f,%16f'%(r1,r2,r3))