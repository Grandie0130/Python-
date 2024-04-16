# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:03:33 2024

@author: User
"""

x = int(input())
y = int(input())
tall = x/100
#計算並印出bmi
BMI = y/ tall**2
print('%.2f'%BMI)

#分類bmi
cat = ['Underweight', 'Normal', 'Overweight', 'Obese Class I', 
       'Obese Class II', 'Obese Class III']
turn = [0, 18.5, 24, 27, 30, 35]
i = 0
while True:
    if BMI >= turn[i] and BMI < turn[i+1]:
        print(cat[i])
        break
    elif BMI >= 35:
        print(cat[5])
        break
    else:
        i += 1
