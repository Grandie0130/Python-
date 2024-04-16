# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:16:44 2024

@author: User
"""

n = int(input())

#重覆印n層
for count in range(n):
    #印n-i個空格
    for co1 in range(n - count - 1):
        print(' ', end = '')
    #印i個星號
    for co2 in range(count + 1):
        print('*', end = '')
        if co2 < count:
            print(' ', end = '')
    #換行
    print()