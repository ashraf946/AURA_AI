# =====================================================
# FORCE PROJECT ROOT INTO PYTHON PATH (MUST BE FIRST)
# =====================================================
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st

from app.response_v2 import generate_response_v2
from app.context import ContextMemory

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AURA AI v2",
    page_icon="✨",
    layout="centered"
)

# =====================================================
# HEADER
# =====================================================
st.markdown("<h1 style='text-align:center;'>✨ AURA AI v2</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>A human-like, conversational AI assistant</p>",
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
        "user_name": "Ashraf",
        "last_sentiment": None
    }

if "context" not in st.session_state:
    st.session_state.context = ContextMemory()

# =====================================================
# INPUT (CHATGPT STYLE)
# =====================================================
user_input = st.text_input(
    "Message AURA AI",
    placeholder="Ask anything…"
)

if st.button("Send"):
    if user_input.strip():
        reply = generate_response_v2(
            user_input,
            st.session_state.memory,
            st.session_state.context
        )

        st.session_state.chat_history.append({
            "user": user_input,
            "bot": reply
        })

# =====================================================
# CHAT DISPLAY (CHATGPT STYLE Q → A)
# =====================================================
st.markdown("### 💬 Conversation")

for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AURA AI:** {chat['bot']}")
    st.markdown("---")

# =====================================================
# FOOTER
# =====================================================
st.caption("⚡ AURA AI v2 | Extreme Edition | Built by Ashraf")
