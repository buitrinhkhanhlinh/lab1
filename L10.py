# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:28:28 2024

@author: LENOVO
"""


a = int(input("Nhập số xe của bạn (4 chữ số): "))
n = (a // 1000 + (a // 100) % 10 + (a // 10) % 10 + a % 10) % 10
print("Số xe của bạn được",n,"nút")
