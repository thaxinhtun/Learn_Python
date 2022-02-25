# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:30:09 2021

@author: SC
"""

meters = 640
inches = (meters * 100) / 2.54
feet = inches/12.0
yards = feet/3.0
miles = yards/1760.0

print("""
      meter = %d m
      inches = %.4f 
      feet = %.4f
      yards = %.4f
      miles = %.4f
      """ %(meters, inches, feet, yards, miles)
      )
