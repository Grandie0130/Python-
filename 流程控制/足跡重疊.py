# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:22:52 2024

@author: User
"""
from math import sqrt

#定義判別距離的函式
def A():
    hori = pow(x-x1, 2)
    verti = pow(y-y1, 2)
    dis = sqrt(hori + verti)
    if dis <= r1:
        return True
    else:
        return False
def B():
    hori = pow(x-x2, 2)
    verti = pow(y-y2, 2)
    dis = sqrt(hori + verti)
    if dis <= r2:
        return True
    else:
        return False

#輸入資料，每個xy判斷完就洗掉
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
n = int(input())
a = b = a_b = 0
for count in range(n):
    x, y = map(int, input().split())
    A()
    B()
    #開始判別，然後放入計數
    if A() == True and B() == True:
        a_b += 1
    elif A() == True:
        a += 1
    elif B() == True:
        b += 1
#印出結果
left = n - a - b - a_b
seq = [a_b, a, b, left]
for count in seq:
    print(count)

    