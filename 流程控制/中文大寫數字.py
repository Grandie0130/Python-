# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:08:59 2024

@author: User
"""

x = int(input())

chinese = {1:'壹', 2:'貳', 3:'參', 4:'肆', 5:'伍', 6:'陸',
           7:'柒', 8:'捌', 9:'玖', 0:''}
dig_names = {4:'萬', 3:'仟', 2:'佰', 1:'拾'}

if x < 1 or x > 99999:
    print('out of range')
else:

    #切出每個位數
    digits = []
    while x > 0:
        num = x % 10
        digits.append(num)
        x = x // 10
    
    #從萬開始印
    i = len(digits) - 1
    while i >= 0:
        print(chinese[digits[i]], end = '')
        if i > 0 and digits[i] != 0:
            print(dig_names[i], end = '')
        i -= 1
    print('元整')
            