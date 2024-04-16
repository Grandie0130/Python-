# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:48:48 2024

@author: User
"""

x = int(input())

if x < 4:
    print(x)
else:
    free = 0
    paid = x
    #一直換一直爽
    while (free + paid) >= 3:
        paid = paid - 4
        max(paid, 0)
        free += 1
    
    print(x+free)
    
