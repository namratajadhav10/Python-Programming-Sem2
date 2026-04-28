# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:01:42 2026

@author: namrata jadhav
"""
# Traffic Police Overspeed Check

speed = int(input("Enter vehicle speed (in km/h): "))

if speed > 60:
    print("Overspeeding! You have to pay a fine.")
else:
    print("Speed is within limit. Drive safely!")