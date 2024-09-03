# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:45:34 2024

@author: LENOVO
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))


if a > b:
    a, b = b, a  
if a > c:
    a, c = c, a  
if b > c:
    b, c = c, b  


print("Các số theo thứ tự tăng dần:",a,b,c)
