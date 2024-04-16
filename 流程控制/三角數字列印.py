# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:04:31 2024

@author: User
"""

n = int(input())

i = 0
num = 0
#重覆印i層
while i < n:
    i += 1
    k = i
    #重覆印k次，並且每次都增加num
    while k > 0:
        num += 1
        print(num, end = ' ')
        k -= 1
    print()
        