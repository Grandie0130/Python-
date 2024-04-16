# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:57:23 2024

@author: User
"""

x = int(input())

#存入所有樓層
i = 0
floors = []
while i < x:
    i += 1
    floors.append(i)

#去掉四樓後印出來
j = 0
if i >= 4:
    floors.remove(4)
    while j < i-1:
        print('floor',floors[j])
        j += 1
else:
    while j < i:
        print('floor', floors[j])
        j += 1