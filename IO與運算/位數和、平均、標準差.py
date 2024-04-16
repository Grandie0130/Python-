# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:55:02 2024

@author: User
"""

from math import sqrt

A = int(input())
B = int(input())
C = float(input())

#抽出各個位數，並分配給名稱
def extract(num):
    digit1 = int(num/1000%10)
    digit2 = int(num/100%10)
    digit3 = int(num/10%10)
    digit4 = int(num%10)
    return digit1, digit2, digit3, digit4
    
A1, A2, A3, A4 = extract(A)
B1, B2, B3, B4 = extract(B)
C1, C2, C3, C4 = extract(C)

#定義計算的函式
def P(num):
    power2 = (num)**2
    return power2

def Cal(x, y, z):
    Sum = x+y+z
    Ave = Sum/3
    VarW = P(x-Ave)+P(y-Ave)+P(z-Ave)
    Sd = sqrt(VarW/3)
    return Sum, Ave, Sd

#計算和、平均、標準差
thousand = Cal(A1, B1, C1)
hundred = Cal(A2, B2, C2)
ten = Cal(A3, B3, C3)
one = Cal(A4, B4, C4)
total = Cal(A, B, C)

#按照格式印出來
def Print1(List):
    print('%d %.2f %.2f'%(List[0], List[1], List[2]))
def Print2(List):
    print('%.2f %.2f %.2f'%(List[0], List[1], List[2]))
    
Print1(thousand)
Print1(hundred)
Print1(ten)
Print1(one)
Print2(total)

