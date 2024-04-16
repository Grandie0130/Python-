# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:30:19 2024

@author: User
"""


def p(num):
    if num == 1:
        print('True')
    else:
        print('False')

a = int(input())
b = int(input())
c = int(input())

repeat1 = 0
repeat2 = 0


if max(a,b,c) == a:
    p(1)
    repeat1 = 1
else:
    p(0)
    
if min(a,b,c) == a:
    p(1)
    repeat2 = 1
else:
    p(0)
    
if repeat1 == 0:
    p(1)
else:
    p(0)
    
if repeat2 == 0:
    p(1)
else:
    p(0)