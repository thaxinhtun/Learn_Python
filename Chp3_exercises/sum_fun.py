# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:01:25 2021

@author: SC
"""


def sum_1k(M):
    s=0
    for k in range(1,M+1):
        s += 1.0/k
    return s

def test_sum_1k():
    tol=1E-14
    expected = 1.83333333333333333333333
    computed = sum_1k(3)
    success = abs(expected - computed)<tol
    msg = "expected %s != computed %s" %(expected,computed)
    
    if(success ==True ):
        print('test pass')
    else:
        print('test fail')
    assert success,msg
    
test_sum_1k()
print(sum_1k(3))