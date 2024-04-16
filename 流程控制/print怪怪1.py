# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:29:36 2024

@author: User
"""

x = int(input())
num = []
i = 0
while i < x:
    y = int(input())
    num.append(y)
    i += 1

#印出數字和換行
j = 0
while j < len(num):
    print(num[j])
    k = 0
    while k < num[j]:
        print()
        k += 1
    j += 1
print("--------------------")