# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:48:54 2024

@author: User
"""

x = int(input())
num = []
while x != -1:
    num.append(x)
    x = int(input())

#印出數字和換行
j = 0
while j < len(num):
    w = len(num)-j-1
    print(num[w])
    k = 0
    while k < num[w]:
        print()
        k += 1
    j += 1
print("--------------------")