# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:16:52 2026

@author: namrata jadhav
"""

#taking list input from the user 
n=int(input("enter number of element;"))
numbers=[]
for i in range(n):
    num=int(input(f"enter element {i+1}:"))
    numbers.append(num)
    # Calculating sum and average 
    total = sum(numbers)
    average=total /n if n> 0 else 0
    print("list:",numbers)
    print("sum of element:",total)
    print("Average of element:", average)