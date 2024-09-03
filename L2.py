# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:58:28 2024

@author: LENOVO
"""

#bai 2
a = int(input('nhap so: '))
b = int(input('nhap so: '))
t = a+b
if a>b:
    h = a-b
else:
    h = b-a
ti = a*b
th = a/b
ch = a//b
print ('tinh tong: ', t)
print ('tinh hieu: ', h)
print ('tinh tich: ', ti)
print ('tinh thuong:', round(th,3))
print ('chia het: ', ch)