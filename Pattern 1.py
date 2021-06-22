# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:29:31 2021

@author: Lenovo
"""

num = int(input("Enter the Number"))
for i in range(1 , num+1):
    for j in range(1 , i+1):
        print("*" , end="")
    print()