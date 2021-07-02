# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:11:06 2021

@author: Lenovo
"""

i = 0 
j = 6
for row in range(4):
    for col in range(7):
        if row==col:
            print("*" , end="")
        elif row==i and col==j:
            print("*" , end="")
            i = i+1
            j = j-1
        else:
            
            print(end=" ")
    print()