import streamlit as st

st.set_page_config(page_title="AURA AI", layout="centered")

st.title("🤖 AURA AI")

user_input = st.text_input("Say something:")

if user_input:
    st.write("You said:", user_input)
    st.write("AURA AI:", "Hello 👋 I am alive on Streamlit Cloud!")
