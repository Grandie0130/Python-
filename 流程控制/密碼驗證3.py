# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:44:24 2024

@author: User
"""

password = input()

#把所有輸入放進list中
tries = []
while True:
    ans = input()
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