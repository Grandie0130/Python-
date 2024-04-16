# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:21:01 2024

@author: User
"""

x = int(input())
y = int(input())
z = int(input())

Sum = x+y+z
Ave = Sum / 3
Pro = x*y*z
Min = min(x, y, z)
Max = max(x, y, z)

"""
sum is 54
average is 18.00
product is 4914
smallest is 13
largest is 27
"""

print('sum is %d'%Sum)
print('average is %.2f'%Ave)
print('product is %d'%Pro)
print('smallest is %d'%Min)
print('largest is %d'%Max)