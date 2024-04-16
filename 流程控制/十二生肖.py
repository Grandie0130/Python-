# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:12:24 2024

@author: User
"""

dic =   {4:'鼠',5:'牛',6:'虎',7:'兔',8:'龍',9:'蛇',10:'馬',11:'羊',0:'猴',1:'雞',2:'狗',3:'豬'}
 
def Year_Checker(n,minguo = False):  #預設西元年(minguo)
    #n必須是整數(int)
    #minguo(代表民國年)
    if minguo == False:
        index = n % 12
        return dic[index]
    elif minguo == True:
        index = (n+1911) % 12
        return dic[index]

#持續輸入中～
x = input()
years = []
while True:
    y = input()
    if y == '-1':
        break
    else:
        years.append(int(y))

#按照西、民判斷
j = 0
checked = []
while x == 'AD' and j < len(years):
    a = Year_Checker(years[j])
    checked.append(a)
    j += 1
while x != 'AD' and j < len(years):
    b = Year_Checker(years[j], minguo = True)
    checked.append(b)
    j += 1
    
#照順序print出來
i = 0
while i < j:
    print(checked[i])
    i += 1
