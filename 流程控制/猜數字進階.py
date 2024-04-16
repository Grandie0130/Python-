# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:47:09 2024

@author: User
"""

ans = int(input())
print('%d < ? < %d'%(1, 100))
x = int(input())

def P():
    print('%d < ? < %d'%(Min, Max))

Min = 1
Max = 100
while x != ans:
    if x <= Min or x >= Max:
        print('out of range')
        P()
    elif x > ans:
        print('wrong answer, guess smaller')
        Max = x
        P()
    else:
        print('wrong answer, guess larger')
        Min = x
        P()
    x = int(input())

print('bingo answer is %d'%ans)