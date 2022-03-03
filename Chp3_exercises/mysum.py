# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:46:02 2021

@author: SC
"""

def mysum(mylist):
    s=0
    str1=""
    list1=[]
    
    if type(mylist[0]) is int:
        for i in mylist:
            s += i
        print(s,'\n')
        
    elif type(mylist[0]) is str:
        for i in mylist:
            str1 += i
        print(str1)
        
    else:
        for i in mylist:
            for j in i:
                list1.append(j)
        print(list1,'\n')
                
mysum([1,3,5,-5])
#4
mysum([[1,2], [3,4], [8,1],[10,9,7]])
#[1, 2, 4, 3, 8, 1]
mysum(['Hello ', 'World'])
#’Hello, World!’
