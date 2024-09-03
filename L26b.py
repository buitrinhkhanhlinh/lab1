# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:49:26 2024

@author: LENOVO
"""



N = int(input("Nhập số nguyên N (tối đa 4 chữ số): "))

a = N // 1000  
b = (N // 100) % 10  
c = (N // 10) % 10  
d = N % 10  

if a > b: a, b = b, a
if a > c: a, c = c, a
if a > d: a, d = d, a

if b > c: b, c = c, b
if b > d: b, d = d, b

if c > d: c, d = d, c

A = str(a) + str(b) + str(c) + str(d)

print("Số có các chữ số theo thứ tự tăng dần:",A)