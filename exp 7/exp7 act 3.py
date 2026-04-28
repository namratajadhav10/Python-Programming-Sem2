# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:19:28 2026

@author: namrata jadhav
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        grade = self.calculate_grade()
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)


# Example usage
# %%
s1 = Student("Namrata", 82)

s1.display()