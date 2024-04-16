# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:54:54 2024

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
    print(back[i])