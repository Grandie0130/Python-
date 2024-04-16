# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:25:49 2024

@author: User
"""

x = int(input())

if x != 1 and x != 2:
    print('role error')
else:
    y = int(input())
    
    #學籍正確，開始判別分數
    if y < 0 or y > 100:
        print('score error')
    elif x == 1:
        if y >= 60:
            print('pass')
        else:
            print('fail')
    else:
        if y >= 70:
            print('pass')
        else:
            print('fail')