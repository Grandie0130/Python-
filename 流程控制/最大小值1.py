# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:23:22 2024

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
max_id = min_id = j = k = 0
Min = min(nums)
Max = max(nums)
while j < len(nums):
    if Max == nums[j]:
        max_id = j+1
        break
    j += 1
while k < len(nums):
    if Min == nums[k]:
        min_id = k+1
        break
    k += 1
    
print('%d %d'%(Max, max_id))
print('%d %d'%(Min, min_id))