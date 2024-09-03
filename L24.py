# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:06:58 2024

@author: LENOVO
"""

g = int(input("Nhập giờ: "))
p = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))


if 0 <= g < 24 and 0 <= p < 60 and 0 <= s < 60:
    print(g,"Giờ",p,"phút",s,"giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ.")