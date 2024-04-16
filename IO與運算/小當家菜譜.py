# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:09:42 2024

@author: User
"""

Input = input().split()
N = int(Input[0])
X = int(Input[1])
Y = int(Input[2])
temp = 20

if N%2 == 0:
    temp = temp + X * N/2
    temp = temp - Y * (N/2 - 1)
else:
    temp = temp + X * (N+1)/2
    temp = temp - Y * (N-1)/2
    
print(int(temp))