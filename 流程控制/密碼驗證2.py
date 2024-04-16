# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:25:53 2024

@author: User
"""

password = int(input())

if password <= 0 or password >=2000000000:
    print('Wrong Password Setting!')
else:
    #把所有輸入放進list中
    tries = []
    while True:
        ans = int(input())
        if ans != password:
            tries.append(ans)
        else:
            break
    
    #印出所有結果
    i = 0
    while i < len(tries):
        print('Wrong Password!')
        i += 1
    print('Correct!')
        