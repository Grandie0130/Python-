# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:11:43 2024

@author: User
"""

x = int(input())

i = 0
while i < x:
    j = 0
    while j < x:
        print('*', end = ' ')
        j += 1
    print()
    i += 1