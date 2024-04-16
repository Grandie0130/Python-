# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:51:59 2024

@author: User
"""

x = int(input())

if x > 12 or x <1:
    print("Month doesn't exist!")
else:
    if x <= 2:
        print('Winter')
    elif x <= 5:
        print('Spring')
    elif x <= 8:
        print('Summer')
    elif x <= 11:
        print('Autumn')
    else:
        print('Winter')