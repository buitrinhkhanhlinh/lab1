# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:56:00 2024

@author: LENOVO
"""

a = int(input('nhap so duong co 2 chu so: '))
if 10 <= a <= 99:    
    b = a//10
    c = a%10
    print("ket qua: ", b+c)