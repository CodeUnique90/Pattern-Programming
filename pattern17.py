# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:43:54 2021

@author: Lenovo
"""

for row in range (7):
    for col in range(5):
        if col==0 or (row==6 and col>0):
            print("*" , end="")
        print(end=" ")
    print()