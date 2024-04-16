# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:28:09 2024

@author: User
"""

x = input()
record = []
while x != 'q':
    record.append(x)
    x = input()

#印出所有記錄和q
i = 0
while i < len(record):
    print('%s'%record[i])
    i += 1
print('%s'%('q'))    