# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:51:49 2026

@author: namrata jadhav 
"""


import streamlit as st

# Title of the app
st.title("Grocery Bill Calculator")

# User inputs
item1 = st.text_input("Enter Item 1 Name")
price1 = st.number_input("Enter Item 1 Price", min_value=0.0)

item2 = st.text_input("Enter Item 2 Name")
price2 = st.number_input("Enter Item 2 Price", min_value=0.0)

item3 = st.text_input("Enter Item 3 Name")
price3 = st.number_input("Enter Item 3 Price", min_value=0.0)

# Button
if st.button("Generate Bill"):

    # Calculate total bill
    total = price1 + price2 + price3

    # Display bill
    st.subheader("Grocery Bill")

    st.write(item1, ":", "₹", price1)
    st.write(item2, ":", "₹", price2)
    st.write(item3, ":", "₹", price3)

    st.success(f"Total Bill Amount = ₹{total}")