# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:07:03 2024

@author: LENOVO
"""

def check(arr):
    count=0
    for i in arr:
        if(i%4==0 & i%6==0):
            print(i,end=' ')
            count+=1
    return count  
arr=list(map(int,input().split()))
#arr=[1,36,24,9,2,12]
print("the count is:",check(arr))