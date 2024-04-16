# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:56:33 2024

@author: User
"""

x = int(input())

Sum = i = 0
num = []
while i <= x:
    Sum =Sum + i
    num.append(str(i))
    i += 1

num.remove('0')
plus = '+'.join(num)
print('%s = %d'%(plus, Sum))