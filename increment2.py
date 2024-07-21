# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:47:26 2024

@author: LENOVO
"""

def check(ele):
    ele=str(ele)
    return ele==ele[::-1]
def increment(arr):
    count=0
    for ele in arr:
        if check(ele):
            print(ele)
            count+=1
    return count
arr=[21,78,212,782,1001]
print(increment(arr))