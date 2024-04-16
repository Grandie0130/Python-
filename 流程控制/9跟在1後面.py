# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:10:51 2024

@author: User
"""
#連續輸入，並照順序存起來
n = input()
nums = []
while n != 'q':
    nums.append(int(n))
    n = input()
    
#判斷9跟在1後面
i = 1
amount = 0
while i < len(nums):
    if nums[i] == 9 and nums[i-1] == 1:
        amount += 1
    i += 1
print(amount)
    
        