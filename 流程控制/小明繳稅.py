# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:54:46 2024

@author: User
"""

N = int(input())

#級距、稅率、差額
R = [0, 540000, 1210000, 2420000, 4530000, 10310000]
J = [5, 12, 20, 30, 40, 45]
L = [0, 37800, 134600, 376600, 829600, 1345100]
#稅金，M直接最後再(K-L)就好
K = []
i = 0
while i < len(J):
    K.append(int( N * J[i] / 100))
    i += 1
    
#全部改成由大到小
change = [R, J, K, L]
for count in change:
    count.sort(reverse = True)

#檢查小明在哪個級距，印出相應的JKLM
def P(n):
    print(J[n], '%', sep = '', end = ' ')
    print(K[n], end = ' ')
    print(L[n], end = ' ')
    print(K[n]-L[n], end = ' ')

i = 0
for check in R:
    if N > check:
        P(i)
        break
    i += 1
    