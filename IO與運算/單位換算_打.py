# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:30:26 2024

@author: User
"""

x = int(input())

doz = x//12
left = x%12

if(left==0):
    print(doz,'dozen')
else:
    print(doz, 'dozen and', left)