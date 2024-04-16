# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:48:56 2024

@author: User
"""
data = input().split()
N = int(data[0])
M = int(data[1])

ch = 2*N
ra = 4*N

if M < 2*N:
    print('NO')
else:
    chTRUE = (ra - M)/2
    raTRUE = N - chTRUE
    
    if chTRUE%1==0 and raTRUE%1==0:
        print('YES')
        print(int(chTRUE), int(raTRUE))
    else:
        print('NO')


#下面是用方程式組的解法，省不得刪掉……
"""
from sympy import symbols, Eq, solve

data = input().split()
N = int(data[0])
M = int(data[1])

#解二元一次方程式組
x, y = symbols('x, y')
eq1 = Eq(x+y, N)
eq2 = Eq(2*x+4*y, M)
sol = solve([eq1, eq2], (x, y))

#把dictionary資料轉成數字
values = list(sol.values())
chicken = values[0]
rabbit = values[1]

#看是否為整數解，來決定要輸出什麼
if chicken%1==0 and rabbit%1==0:
    print('YES')
    print(chicken, rabbit)
else:
    print('NO')
    
"""


