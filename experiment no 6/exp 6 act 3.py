# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:56:28 2026

@author: namrata jadhav
"""



file = open("complaints.txt", "w")
file.write("Late service\nPoor quality\nDelay in response")
file.close()

file = open("complaints.txt", "r")
data = file.read()
print("Complaints:\n", data)
file.close()