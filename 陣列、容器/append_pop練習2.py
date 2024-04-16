# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:36:41 2024

@author: User
"""

n = int(input())
string = []

for i in range(n):
    x = input()
    string.append(x)

for i in range(n):
    j = n - 1 - i
    print('data %s'%string[j])