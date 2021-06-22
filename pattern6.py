# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 01:26:38 2021

@author: Lenovo
"""

for row in range(7):
    for col in range(5):
        if ((col == 0 or col ==4) and row!=0) or ((row == 0 or row== 3) and (col>0 and col<4)):
            print("*" , end="")
        else:
            print(end=" ")
    print()