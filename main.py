import streamlit as st
from backend import chat_with_gemini

st.markdown(
    """
    <style>
    body {
        background-color: #eef2f7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .chat-container {
        padding: 20px;
        border-radius: 12px;
        background: white;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .user-bubble {
        background: linear-gradient(135deg, #6ea8fe, #1a73e8);
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 0 18px;
        margin: 8px 0;
        max-width: 70%;
        margin-left: auto;
        word-wrap: break-word;
        font-size: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        animation: fadeInUp 0.3s ease-in-out;
    }
    .bot-bubble {
        background: #f8f9fa;
        color: #333;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 0;
        margin: 8px 0;
        max-width: 70%;
        margin-right: auto;
        word-wrap: break-word;
        font-size: 15px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        animation: fadeInUp 0.3s ease-in-out;
    }
    .title {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #1a73e8;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "conversation" not in st.session_state:
    st.session_state.conversation = []

st.markdown("<div class='title'>💬 AI Chatbot</div>", unsafe_allow_html=True)

for msg in st.session_state.conversation:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>{msg['parts'][0]}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>{msg['parts'][0]}</div>", unsafe_allow_html=True)

user_input = st.chat_input("Type your message here...")

if user_input:
    
    st.session_state.conversation.append({"role": "user", "parts": [user_input]})
    st.markdown(f"<div class='user-bubble'>{user_input}</div>", unsafe_allow_html=True)

    reply = chat_with_gemini(user_input)
    st.session_state.conversation.append({"role": "assistant", "parts": [reply]})
    st.markdown(f"<div class='bot-bubble'>{reply}</div>", unsafe_allow_html=True)
