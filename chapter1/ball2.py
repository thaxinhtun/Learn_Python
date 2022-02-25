# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:11:34 2021

@author: SC
"""
#initialize values

g = 9.81 # m/s**2
v0 = 15 # km/h
theta = 60 #degrees
x = 0.5 # m
y0 = 1 # m

print ("""v0 = %.1f km/h
theta = %d degrees
y0 = %.1f m
x = %.1f m""" % (v0, theta, y0, x))

#unit conversion

v0 = v0/3.6
from math import *
theta = theta*pi/180

#compute y

y = x*tan(theta) - 1/(2*v0)*g*x**2/((cos(theta))**2) + y0

print('y = %.1f m'% y)

