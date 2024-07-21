# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 05:57:17 2024

@author: LENOVO
"""

n=1729
original=n
sum=0
while n>0:
	rem=n%10
	sum=sum+rem
	n=n//10

a=sum

sumrev=0
product=0
while sum>0:
	rem=sum%10
	sumrev=sumrev*10+rem
	sum=sum//10
    
product= a*sumrev

if product==original:
	print("magical number")
else:
	print("not magical")