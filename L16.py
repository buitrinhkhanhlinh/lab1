# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:48:28 2024

@author: LENOVO
"""

import re


a = input("Nhập thời gian: ")


h = re.search(r'(\d+)h', a)
m = re.search(r'(\d+)p', a)
s = re.search(r'(\d+)s', a)

h = int(h.group(1)) if h else 0
m = int(m.group(1)) if m else 0
s = int(s.group(1)) if s else 0

t = h * 3600 + m * 60 + s

print("Tổng số giây là: ",t)
