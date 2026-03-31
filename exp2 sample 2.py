# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:58:12 2026

@author: namrata jadhav
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
  fact = fact * i
print("Factorial:", fact)