# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:34:31 2024
 
@author: User
"""
"""
M是(0, M-1)的水平範圍
N是(0, N-1)的垂直範圍
X1 Y1是R1的初始座標
E1 N1是R1要先向北走N1，再向東走N1
X2 Y2是R2的初始座標
E2 N2是R2要先向東走E2，再向北走N1
F1 F2是R1、R2有的燃料
"""

M,N,X1,Y1,E1,N1,F1,X2,Y2,E2,N2,F2 = map(int, input().split())

#設定機器人走每一步時的通用函式
def run(step, point, fuel, direction):
    step -= 1
    fuel -= 1
    point += 1
    if point == direction:
        point = 0
    return step, point, fuel

#備份每次循環的步數
n1 = N1
n2 = N2
e1 = E1
e2 = E2
 
#時間最多只會到 max(F1,F2)，可能會提早爆炸
time = max(F1, F2)
explode = False
moment = 0
for i in range(time):
    #第 i 秒時R1的行動
    if F1 > 0:
        if N1 > 0:
            #先往北走
            N1, Y1, F1 = map( int, run(N1, Y1, F1, N) )
        else:
            #再往東走
            E1, X1, F1 = map( int, run(E1, X1, F1, M) )
    #第 i 秒時R2的行動
    if F2 > 0:
        if E2 > 0:
            #先往東走
            E2, X2, F2 = map( int, run(E2, X2, F2, M) )
        else:
            #再往北走
            N2, Y2, F2 = map( int, run(N2, Y2, F2, N) )

    #直到爆炸才提早結束迴圈
    if X1 == X2 and Y1 == Y2:
        explode = True
        moment = i+1
        break
    #步數走完了話，就重置步數
    if E1 == N1 == 0:
        E1 = e1
        N1 = n1
    if E2 == N2 == 0:
        E2 = e2
        N2 = n2
 
if explode == False:
    print('robots will not explode')
else:
    print('robots explode at time %d'%moment)