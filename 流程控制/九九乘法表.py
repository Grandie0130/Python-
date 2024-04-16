# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:33:42 2024

@author: User
"""

m = int(input())
n = int(input())

i = 0
while i < m:
    i += 1
    j = 0
    while j < n:
        j += 1
        product = i*j
        print('%d*%d=%2d'%(i, j, product), end = ' ')
    print()