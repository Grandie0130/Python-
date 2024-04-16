# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:02:24 2024

@author: User
"""

n = int(input())

i = 0
p = ''
back = []
while i < n:
    p = p + '*'
    back.append(p)
    i += 1

while i > 0:
    i -= 1
    j = n-i
    #先迴圈印出*以前的所有空白，再印星號
    while j > 1:
        print(' ', end = '')
        j -= 1
    print(back[i])