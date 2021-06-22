# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 01:25:03 2021

@author: Lenovo
"""


num = int(input("Enter the number"))
for i in range(0 , num):
    for j in range(0 , num-i-1):
        print(end=" ")
    for j in range (0 , 2*i+1):
        print("*" , end=" ")
    print()