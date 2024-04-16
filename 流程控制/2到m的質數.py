# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:49:56 2024

@author: User
"""
from math import sqrt

m = int(input())

#判別出所有質數
num = 2
primes = []
while num <= m:
    #找出大於平方根的因數數量，如果是質數應該只有1個
    factor = num
    checked = []
    while factor >= sqrt(num):
        if num % factor == 0:
            checked.append(factor)
        factor -= 1
    if len(checked) == 1:
        primes.append(num)
    num += 1

#印出所有結果
def P(n):
    print('%d is prime'%n)
    
i = 0
while i < len(primes):
    P(primes[i])
    i += 1