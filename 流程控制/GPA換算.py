# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:35:20 2024

@author: User
"""

x = int(input())
GPA = {4.3:'A+', 4.0:'A', 3.7:'A-', 3.3:'B+', 3.0:'B', 2.7:'B-',
       2.3:'C+', 2.0:'C', 1.7:'C-', 0:'F'}
turn = [90, 85, 80, 77, 73, 70, 67, 63, 60, 0]
gpa = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0]

i = 9
while True:
    if x >= turn[i] and x <= turn[i-1]:
        print(gpa[i])
        print(GPA[gpa[i]])
        break
    elif x >= turn[0]:
        print(gpa[0])
        print(GPA[gpa[0]])
        break
    else:
        i -= 1