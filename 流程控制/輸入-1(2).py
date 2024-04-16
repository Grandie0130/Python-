# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:23:41 2024

@author: User
"""

x = int(input())
num = {}
id = 0
while x != -1:
    id += 1
    num[id]=int(x)
    x = int(input())

#計算總和、平均
Sum = Ave = i = 0
while i < len(num):
    i += 1
    Sum = Sum + num[i]
    Ave = Sum/i

#找出最大值/最小值和他們的位置
Max = max(num.values())
Max_id = 1
while num[Max_id] < Max:
    Max_id += 1
Min = min(num.values())
Min_id = 1
while num[Min_id] > Min:
    Min_id += 1
    
print(Sum)
print('%.1f'%Ave)
print(Max)
print(Max_id)
print(Min)
print(Min_id)
