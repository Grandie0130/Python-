# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:59:36 2024

@author: User
"""

#連續輸入
x = int(input())
i = 0
nums = []
while i < x:
    y = int(input())  
    nums.append(y)
    i += 1

#找最大值、最小值的位置
max_id = []
min_id = []
j = k = 0
Min = min(nums)
Max = max(nums)
while j < len(nums):
    if Max == nums[j]:
        max_id.append(j + 1)
    j += 1
while k < len(nums):
    if Min == nums[k]:
        min_id.append(k + 1)
    k += 1
    
if len(max_id) > 1:
    last = len(max_id) - 1
    print('%d %d %d'%(Max, max_id[0], max_id[last]))
else:          
    print('%d %d'%(Max, max_id[0]))
    
if len(min_id) > 1:
    last = len(min_id) - 1
    print('%d %d %d'%(Min, min_id[0], min_id[last]))
else:
    print('%d %d'%(Min, min_id[0]))