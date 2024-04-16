# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:19:46 2024

@author: User
"""

n = int(input())
half = int( (n + 1) / 2 )

#聖誕樹的星星
for count in range(n-1):
    print(' ', end = '')
print('*')

#聖誕樹的葉子，總共有n-2層
for count in range(n-2):
    #每層固定是3行，每層的start的星數是2n+1
    start = 2 * count + 1
    for co1 in range(3):
        #先印(i-3)個空格，再開始少量空格和星號
        same_space = n - 3 - count
        for co2 in range(same_space):
            print(' ', end = '')
        #(2-i)個空格，然後星號
        for co2 in range(2 - co1):
            print(' ', end = '')
        #葉子的數量跟換行
        for co2 in range(start):
            print('^', end = '')
        start = start + 2
        print()

#聖誕樹幹有多高
for count in range(n-2):
    #有多粗
    for co1 in range(half):
        print(' ', end = '')
    for co2 in range(n-2):
        print('#', end = '')
    print()