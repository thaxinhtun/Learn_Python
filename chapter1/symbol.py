# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:56:35 2021

@author: SC
"""

from sympy import *
t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y,t)
print('velocity: ', dydt)
print('acceleration: ',diff(y,t,t))
print('position: ',integrate(dydt,t))