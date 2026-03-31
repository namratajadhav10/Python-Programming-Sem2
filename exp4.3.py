# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:16:07 2026

@author: namrata jadhav
"""



# Program to reverse a customer feedback message

# Input feedback
feedback = input("Enter customer feedback: ")

# Method 1: Reverse characters using slicing
reversed_feedback = feedback[::-1]

# Display results
print(f"Original: {feedback}")
print(f"Reversed: {reversed_feedback}")