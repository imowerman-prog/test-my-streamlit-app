import streamlit as st

st.title("GitHub + Streamlit on Mac 🍎")
st.write("This app lives in a cloned GitHub repo!")

name = st.text_input("Your name?")
if name:
    st.success(f"Hey {name}! You're live on Streamlit!")

st.balloons()