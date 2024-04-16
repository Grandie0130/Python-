# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:08:52 2024

@author: User
"""

n = int(input())

i = 0
while i < n:
    j = n - i
    i += 1
    #印出n-i個空格
    while j > 1:
        print(' ', end = '')
        j -= 1
    #印出i個星號
    k = i
    while k > 0:
        print('*', end = '')
        k -= 1
    print()