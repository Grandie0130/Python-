# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:16:49 2024

@author: User
"""

x = input().split(',')

#抓出所有的數字
total = []
i = 0
while i < len(x):
    total.append(int(x[i]))
    i += 1
    
#各自加總
total_sum = odd_sum = even_sum = 0
while i > 0:
    i -= 1
    total_sum = total_sum + total[i]
    if total[i]%2 != 0:
        odd_sum = odd_sum + total[i]
    else:
        even_sum = even_sum + total[i]

print(odd_sum)
print(even_sum)
print(total_sum)
        


