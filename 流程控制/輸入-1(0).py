# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:34:41 2024

@author: User
"""

x = input()
num = []
while x != '-1':
    num.append(int(x))
    x = input()

Sum = Ave = i = 0
while i < len(num):
    Sum = Sum + num[i]
    Ave = Sum/(i+1)
    i += 1
print(Sum)
print('%.1f'%Ave)
    