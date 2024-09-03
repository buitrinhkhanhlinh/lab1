# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:56:46 2024

@author: LENOVO
"""

a = input("Nhập theo định dạng ngày/tháng/năm, ngày/tháng/năm (2 chữ số) hoặc năm/tháng/ngày: ")

b = a.split('/')

if len(b) == 3:
    if len(b[0]) == 4:
        y = b[0]
        m = b[1]
        d = b[2]
    else:
        d = b[0]
        m = b[1]
        y = b[2]
        if len(y) == 2:
            y = '20' + y

    print("Ngày: ",d,"Tháng: ",m,"Năm: ",y)
else:
    print("Định dạng không hợp lệ.")
    