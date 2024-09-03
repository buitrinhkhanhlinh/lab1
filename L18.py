# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:14:41 2024

@author: LENOVO
"""

def nhap_thoi_gian():
    g = int(input("Nhập giờ: "))
    p = int(input("Nhập phút: "))
    s = int(input("Nhập giây: "))
    return g * 3600 + p * 60 + s 

def hien_thi(tong_giay):
    g = tong_giay // 3600
    p = (tong_giay % 3600) // 60
    s = tong_giay % 60
    print("thời ",g,"giờ",p,"phút",s,"giây")
tg1 = nhap_thoi_gian()
tg2 = nhap_thoi_gian()

hien_thi(tg1 + tg2)
hien_thi(abs(tg1 - tg2))