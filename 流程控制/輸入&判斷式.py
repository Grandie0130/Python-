# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:05:36 2024

@author: User
"""

#持續輸入直到q
num = []
while True:
    x = input()
    if x == 'q':
        break
    else:
        num.append(float(x))

#分到整數區或是小數區
Int = []
Float = []
i = 0
while i < len(num):
    if num[i] % 1 == 0:
        Int.append(num[i])
    else:
        Float.append(num[i])
    i += 1


Flp = Inp = 1
j = k = 0
while j < len(Float):
    Flp = Flp*Float[j]
    j += 1
while k < len(Int):
    Inp = Inp*Int[k]
    k += 1

#印出結果
print('%.2f'%Flp)
print('%d'%Inp)
def P(s):
    print('Float %s Int'%s)
if Flp > Inp:
    P('>')
elif Flp == Inp:
    P('=')
else:
    P('<')

    