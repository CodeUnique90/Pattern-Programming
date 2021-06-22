# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:07:28 2021

@author: Lenovo
"""

def pyramid(Rows):
    for i in range (Rows):
        print(" "*(Rows+1)+"*"*(i+1))
    for j in range(Rows-1 , 0 ,-1):
        print(" "*(Rows-j)+"*"*(j))
        
pyramid(6)





































