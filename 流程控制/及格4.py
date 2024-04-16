# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:38:24 2024

@author: User
"""


#讓使用者可以一直輸入，然後存在不同資料裡
i = 0
scores =[]

while True:
    score = int(input())
    i += 1
    scores.append(score)
    iscontinue = input()
    
    if iscontinue == 'y':
        continue
    else:
        break

#開始印出結果
def grade(num):
    if num >= 60:
        print('pass')
    else:
        print('fail')
        
j = 0
while j < len(scores):
    grade(scores[j])
    j += 1