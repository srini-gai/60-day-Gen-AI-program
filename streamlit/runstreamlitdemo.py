import streamlit as st
st.title("Run streamlit Demo Scripts")
name = st.text_input("Enter your name")

if st.button("Greet Me"):
    if name:
        st.success(f"Hello, {name}! Welcome to Streamlit!")
    else:
        st.error("Please enter your name to be greeted.")

