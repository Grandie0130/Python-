# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:04:07 2024

@author: User
"""

nums = []
for i in range(5):
    x = int(input())
    nums.append(x)
    
for i in range(5):
    print(nums[i], end = '\t')
    for i in range(nums[i]):
        print('*', end = '')
    print()