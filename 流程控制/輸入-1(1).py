# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:40:35 2024

@author: User
"""
x = int(input())
num = {}
id = 0
while x != -1:
    id += 1
    num[id]=int(x)
    x = int(input())

#計算總和、平均
Sum = Ave = i = 0
while i < len(num):
    i += 1
    Sum = Sum + num[i]
    Ave = Sum/i

#找出最大值、位置
Max = max(num.values())
Max_id = 1
while num[Max_id] < Max:
    Max_id += 1
    
print(Sum)
print('%.1f'%Ave)
print(Max)
print(Max_id)


#不知道為什麼Runtime Error，心累……
"""
x = input()
num = []
while x != '-1':
    num.append(int(x))
    x = input()

#計算總合、平均
Sum = Ave = i = 0
while i < len(num):
    Sum = Sum + num[i]
    Ave = Sum/(i+1)
    i += 1

    
#找出最大值和位置
order = []
i = 0
while i < len(num):
    order.append(num[i])
    i += 1

order.sort(reverse=True)
id = 0
while num[id] < order[0]:
    id += 1

#印出結果
print(Sum)
print('%.1f'%Ave)
print(order[0])
print(id+1)
"""