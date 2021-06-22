# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:31:18 2021

@author: Lenovo
"""

num = int(input("Enter the number"))
for i in range(0 , num):
    for j in range(0 , num-i-1):
        print(end=" ")
    for j in range (0 , i+1):
        print("*" , end=" ")
    print()