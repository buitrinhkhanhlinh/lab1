# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:30:58 2024

@author: LENOVO
"""


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))

Min = a  

if b < Min:
    Min = b

if c < Min:
    Min = c

if d < Min:
    Min = d

print("Số nhỏ nhất là:",Min)
