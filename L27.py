# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:05:02 2024

@author: LENOVO
"""

import math

hinh = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if hinh == 'v':
    c = float(input("Nhập độ dài cạnh của hình vuông: "))
    P = 4 * c  
    S = c * c
    print("Chu vi hình vuông P =",P,"Diện tích hình vuông S =",)

elif hinh == 'n':
    cr = float(input("Nhập chiều rộng: "))
    cd = float(input("Nhập chiều dài: "))
    P = 2 * (cd + cr)
    S = cd * cr
    print("Chu vi hình chữ nhật P =",P, "Diện tích hình chữ nhật S =",S)

elif hinh == 't':
    r = float(input("Nhập bán kính: "))
    P = 2 * math.pi * r
    S = math.pi * r * r
    print("Chu vi hình tròn P =",P,"Diện tích hình tròn S =",S)

else:
    print("Loại hình không hợp lệ.")