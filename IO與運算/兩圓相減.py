# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:27:20 2024

@author: User
"""
import math

x = int(input())
y = int(input())

area_x = pow(x,2)*math.pi
area_y = pow(y,2)*math.pi

print('%.2f'%(area_y-area_x))
