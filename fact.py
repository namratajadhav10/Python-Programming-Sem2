# program for factorial 
"""
Created on Tue Feb 10 13:00:16 2026

@author: namrata jadhav
"""
n = int(input("enter number:"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print("factorial:",fact)