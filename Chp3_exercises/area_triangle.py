# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:41:35 2021

@author: SC
"""

def area(vertices):
    return 0.5*abs(vertices[1][0]*vertices[2][1] - vertices[2][0]*vertices[1][1]\
                   -vertices[0][0]*vertices[2][1]+vertices[2][0]*vertices[0][1]\
                       -vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1]
                   )

v1 = (0,0); v2 = (1,0); v3 = (0,2)
vertices = [v1, v2, v3]
triangle1 = area(vertices)
print(triangle1)