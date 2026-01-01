import streamlit as st
from app.brain import generate_reply

st.set_page_config(page_title="AURA AI", layout="centered")

st.title("🤖 AURA AI")

user_input = st.text_input("Say something:")

if user_input:
    reply = generate_reply(user_input)
    st.write("You:", user_input)
    st.write("AURA AI:", reply)
