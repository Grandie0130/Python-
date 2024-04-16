# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:30:58 2024

@author: User
"""

T = int(input())
N = int(input())
List = input().split()

#把list裡的字串都變成整數
n = 0
num = []
while n < len(List):
    num.append(int(List[n]))
    n += 1

#一個一個確認是否為T
i = 0
j = []
while i < len(num):
    if num[i] == T:
        j.append(i+1)
    i += 1
    
#如果有，就一個一個印出結果
if len(j) == 0:
    print('%d is not found.'%T)
else:
    k = 0
    while k < len(j):
        print('Found@%d'%j[k])
        k += 1