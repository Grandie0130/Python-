# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:27:45 2024

@author: User
"""

x = float(input())
y = float(input())
z = input()

r = 0
if z == '+':
    r = x + y
elif z == '-':
    r = x - y
elif z == '*':
    r = x * y
else:
    r = x / y

print('%.2f %s %.2f = %.2f'%(x, z, y, r))