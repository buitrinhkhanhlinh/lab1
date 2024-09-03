# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:09:57 2024

@author: LENOVO
"""

ch = input("Nhập một chữ cái: ")

if ch.islower():
    ch = ch.upper()
else:
    ch = ch.lower()

print("Chữ cái sau khi đổi: ",ch)