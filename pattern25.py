# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:03:25 2021

@author: Lenovo
"""

for row in range(7):
    for col in range(5):
        if col==2 or (row==0 and col!=2):
            print("*" , end="")
        else:
            print(end=" ")
    print()