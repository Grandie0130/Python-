# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:39:33 2024

@author: User
"""


from math import sqrt

x = float(input())
y = sqrt(x)*10
z = round(y-x)

print('Original: %.2f'%x)
print('Adjusted: %.2f(+%d)'%(y,z))