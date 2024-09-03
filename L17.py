# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:36:04 2024

@author: LENOVO
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

print("Số lớn nhất là:", max_num)
print("Số nhỏ nhất là:", min_num)
