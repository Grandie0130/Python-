# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:22:00 2024

@author: User
"""

from math import sqrt

a, b = [float(val1) for val1 in input().split()]
c, d = [float(val2) for val2 in input().split()]
e, f = [float(val3) for val3 in input().split()]
wrong = 0

#檢查是否有三點共線
if a == c and c == e:
    wrong = 1
elif b == d and d == f:
    wrong = 1
elif (c-a)/(e-c) == (d-b)/(f-d):
    wrong = 1

#用海龍公式計算三角形
if wrong == 1:
    print('%.2f'%0)
else:
    line1 = sqrt( abs(a-c)**2 + abs(b-d)**2 )
    line2 = sqrt( abs(c-e)**2 + abs(d-f)**2 )
    line3 = sqrt( abs(a-e)**2 + abs(b-f)**2 )
    s = (line1 + line2 + line3)/2
    
    area = sqrt(s*(s-line1)*(s-line2)*(s-line3))
    print('%.2f'%area)