# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:39:45 2024

@author: User
"""

num = input()
i = 0
j = 0

#先檢查各個位數是否為7
while i < len(num):
    if num[i] == '7':
        print('YES')
        j = 1
        break
    else:
        i += 1

#再檢查是否為7的倍數
if j == 0 and int(num)%7 ==0:
    print('YES')
    j = 1

#最後剩下的就是no了
if j == 0:
    print('NO')