# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:27:49 2024

@author: User
"""

num = input().split()
L = int(num[0])
S = int(num[1])
i = 0
j = 0

#當阿宅要先快轉影片時
while(S<L):
    i += 1
    S = S+5
    if(S == L):
        break
    while(S>L):
        j += 1
        S = S-2

#當阿宅要先倒轉影片時
while(S>L):
    i += 1
    S = S-2
    if(S == L):
        break
    while(S<L):
        j += 1
        S = S+5

print(i+j)