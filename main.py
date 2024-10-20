import streamlit as st

st.title("Hello World")

st.write("This is a simple Streamlit app")

st.write("Here is a button:")
if st.button("Click me"):
    st.write("You clicked the button!")