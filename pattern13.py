# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:28:54 2021

@author: Lenovo
"""

for row in range(7):
    for col in range(6):
        if col==0 or col==4 or(row==3 and(col>0 and col<4)):
            print("*" , end="")
        else:
            print(end=" ")
    print()
