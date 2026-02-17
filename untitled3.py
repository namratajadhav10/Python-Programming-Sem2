# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:26:43 2026

@author: User
"""

name =input("Enter your name:")  #string
age =int(input("Enter your age:"))  #integer 
height =float(input("Enter your height:"))  #float
is_student =input("Are you astudent? (True/False):").lower()=="true"  #Boolean


#printing the inputs
print("\nEntered Details:")
print("Name:",name)
print("Age:", age)
print("Height:", height)
print("Is Student:",is_student)