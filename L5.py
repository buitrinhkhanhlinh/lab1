# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:59:14 2024

@author: LENOVO
"""

a = input("Nhập thời gian theo định dạng hh:mm:ss: ")
hh, mm, ss = map(int, a.split(':'))
T = hh * 3600 + mm * 60 + ss
print("Tổng số giây:", T)
