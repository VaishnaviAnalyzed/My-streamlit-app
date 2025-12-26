import streamlit as st 

st.title ("My First Streamlit App created by Vaishnavi Chandore")

st.write(" Welcome! This app calculates the sqaure of a number.")

st.header("Select a Number")
number = st.slider("Pick a number", 0,100,25)

st.subheader("Result")
squared_number = number * number 
st.write(f"The square of **{number}** is **{squared_number}**.")
