import streamlit as st
from app.brain import generate_reply

# -----------------------------------------------------
# Page configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="AURA AI",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------------------------
# App Title
# -----------------------------------------------------
st.title("🤖 AURA AI")
st.caption("Your personal AI companion")

# -----------------------------------------------------
# Session state for chat history
# -----------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------------------------
# User input
# -----------------------------------------------------
user_input = st.text_input(
    "Say something:",
    placeholder="Type your message here..."
)

# -----------------------------------------------------
# When user sends a message
# -----------------------------------------------------
if user_input:
    # Generate reply from brain
    reply = generate_reply(user_input)

    # Store conversation
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AURA AI", reply))

# -----------------------------------------------------
# Display chat history (ChatGPT-style)
# -----------------------------------------------------
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(
            f"""
            <div style="
                background-color:#2563eb;
                color:white;
                padding:10px;
                border-radius:10px;
                margin-bottom:8px;
                text-align:right;
            ">
            {message}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color:#1f2937;
                color:white;
                padding:10px;
                border-radius:10px;
                margin-bottom:12px;
                text-align:left;
            ">
            {message}
            </div>
            """,
            unsafe_allow_html=True
        )
