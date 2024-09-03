# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:12:15 2024

@author: LENOVO
"""

import math

def bai(a, b):
    # Tính căn bậc 3 của a và b
    a_bac = math.pow(a, 1/3)
    b_bac = math.pow(b, 1/3)
    
    # Tính các thành phần của biểu thức
    A = (a + b) / (a_bac + b_bac) - math.pow(a * b, 1/3)
    B = math.pow(a_bac - b_bac, 2)
    
    # Tính kết quả cuối cùng
    kq = A / B
    return kq
a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
kq = bai(a, b)
print ("Kết quả:",kq)
