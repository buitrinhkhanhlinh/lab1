# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:36:52 2024

@author: LENOVO
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

if a >= b and a >= c:
    Max = a
elif b >= a and b >= c:
    Max = b
else:
    Max = c
print("Số lớn nhất là:",Max)
