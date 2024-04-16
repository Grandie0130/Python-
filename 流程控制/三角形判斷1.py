# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:50:08 2024

@author: User
"""

a = int(input())
b = int(input())
c = int(input())

#判斷是否為三角形
num = [a, b, c]
num.sort()
if num[0]+num[1] <= num[2]:
    print('False')
else:
    print('True')
    
    #判斷是否為直角
    if num[0]**2 + num[1]**2 == num[2]**2:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')