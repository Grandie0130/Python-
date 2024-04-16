# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:10:09 2024

@author: User
"""

x = int(input())
def check(num):
    if num == 0:
        return True
    else:
        return False
#把每個檢查結果存起來
check_list = []
i = 0
while i <= x:
    i += 1
    y = x % i
    check_list.append(check(y))
    
#看是否有2個以上因數，印出結果
prime_or_not = check_list.count(True)
if prime_or_not == 2:
    print('%d is prime'%x)
else:
    print('%d is not prime'%x)

    
    