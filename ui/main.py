# =====================================================
# FORCE PROJECT ROOT INTO PYTHON PATH (MUST BE LINE 1)
# =====================================================
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# =====================================================
# IMPORTS (ONLY AFTER PATH FIX)
# =====================================================
import streamlit as st
import plotly.express as px

from app.response_engine import generate_response
from data.memory_db import get_all_interactions

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AURA AI",
    page_icon="✨",
    layout="centered"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(
    """
    <style>
    body {
        background-color: #0f172a;
        color: #e5e7eb;
    }
    .chat-user {
        background-color: #2563eb;
        color: white;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        text-align: right;
    }
    .chat-bot {
        background-color: #1f2933;
        color: #e5e7eb;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 20px;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================
st.markdown("<h1 style='text-align:center;'>✨ AURA AI</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Your intelligent, human-like assistant</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# SESSION STATE
# =====================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "memory" not in st.session_state:
    st.session_state.memory = {
        "user_name": None,
        "last_sentiment": None
    }

# =====================================================
# INPUT
# =====================================================
user_input = st.text_input(
    "Type your message",
    placeholder="Talk to AURA AI..."
)

if st.button("Send"):
    if user_input.strip():
        result = generate_response(user_input, st.session_state.memory)

        st.session_state.chat_history.append({
            "user": user_input,
            "bot": result["reply"],
            "intent": result["intent"],
            "sentiment": result["sentiment"]
        })

# =====================================================
# CHAT DISPLAY
# =====================================================
for chat in st.session_state.chat_history:
    st.markdown(
        f"<div class='chat-user'>👤 {chat['user']}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='chat-bot'>
        🤖 {chat['bot']}<br>
        <small>Intent: {chat['intent']} | Sentiment: {chat['sentiment']}</small>
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================
st.markdown("---")
st.subheader("📊 AURA AI Analytics Dashboard")

interactions = get_all_interactions()

if interactions:
    sentiments = [i.sentiment for i in interactions]
    timestamps = [i.timestamp for i in interactions]

    fig1 = px.histogram(
        x=sentiments,
        title="Sentiment Distribution",
        labels={"x": "Sentiment", "y": "Count"},
        color=sentiments
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(
        x=timestamps,
        y=sentiments,
        title="Sentiment Over Time",
        labels={"x": "Time", "y": "Sentiment"}
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No analytics data yet. Start chatting 😊")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("⚡ Powered by AURA AI | Built by Ashraf")
