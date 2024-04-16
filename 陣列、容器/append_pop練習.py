# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:24:53 2024

@author: User
"""

num = int(input())
ns = []

for i in range(num):
    left = num - i
    ns.append(left)

for i in range(num):
    print('data %d'%ns[0])
    right = num - ns[0]
    ns.append(right+1)
    ns.pop(0)
print()
for i in range(num):
    print('data %d'%ns[i])