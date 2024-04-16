# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:44:14 2024

@author: User
"""

x, y = input().split()
n = int(x)
m = int(y)

num1 = []
num2 = []
for num in range(n,m+1):
    #切開每個位數，直接一個一個判斷，不存起來
    have7 = False
    i = num
    while i > 0:
        j = i % 10
        if j == 7:
            have7 = True
            break
        i = i // 10
    #開始判斷
    if num % 7 == 0:
        num1.append(num)
    if have7 == True:
        num2.append(num)

k = 0
while k < len(num1):
    print(num1[k], end = '')
    if len(num1) - k >= 2:
        print(' & ', end = '')
    k += 1
print()
k = 0
while k < len(num2):
    print(num2[k], end = '')
    if len(num2) - k >= 2:
        print(' & ', end = '')
    k += 1