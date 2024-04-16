# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:54:02 2024

@author: User
"""

n = int(input())
half = int( (n+1)/2 )
#重覆印n層
for count in range(n):
    
    #菱形的上半部
    if count < half:
    #印n-i個空格
        for co1 in range(half - count - 1):
            print(' ', end = '')
            #印2i-1個星號
        for co2 in range(2 * (count + 1) - 1):
            print('*', end = '')
    
    #菱形的下半部
    else:
        #印i-half個空格
        for co3 in range(count - half + 1):
            print(' ', end = '')
        #印2(n-i)+1個星號
        for co4 in range( 2 * (n - count) - 1):
            print('*', end = '')
    
    #換行
    print()