# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:17:03 2024

@author: User
"""

def Print(num):
    print('獎金 %d 元'%num)


x = int(input())

if x >= 95:
    Print(2000)
elif(x >= 90):
    Print(1000)
elif(x >= 80):
    Print(500)
else:
    Print(0)
    