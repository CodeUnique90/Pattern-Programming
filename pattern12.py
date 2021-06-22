# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:29:32 2021

@author: Lenovo
"""

for  row in range (7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and col>0):
            print("*" , end="")
        else:
            print(end=" ")
    print()