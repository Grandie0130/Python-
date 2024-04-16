# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:42:58 2024

@author: User
"""

n = int(input())

#山體
i = 0
#總共高n
while i < n:
    i += 1
    #左邊的山壁
    j = n - i
    for count in range(j):
        print(' ', end = '')
    print('/', end = '')
    #第二層的積雪
    if i == 2:
        print('~~', end = '')
        print('\\')
    else:
        #其他的右邊山壁
        for count in range( 2*(i - 1) ):
            print(' ', end = '')
        print('\\')

#底下的河流
for count in range(2):
    for i in range(2 * n):
        print('~', end = '')
    print()