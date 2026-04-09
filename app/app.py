import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="AI Chatbot", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
.block-container {
    max-width: 800px;
    margin: auto;
    padding-top: 2rem;
}

[data-testid="stAppViewContainer"] {
    background-color: #f8fafc;
}

.chat-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}


.user-msg {
    background: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: right;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.bot-msg {
    background: white;
    color: black;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: left;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 10px;
}
.stButton > button {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    transition: 0.3s;
}
            
.stButton > button:hover {
    background-color: #334155;
    color: white;
}
            
.stButton > button:active {
    background-color: #0f172a;
    color: white;
}
            
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1 style='text-align:center;'>🤖 Smart Business Chatbot</h1>
<p style='text-align:center; color:gray;'>Automate customer support instantly</p>
<p style='text-align:center; color:#22c55e;'>● Online • Ready</p>
""", unsafe_allow_html=True)

# --- ONLINE STATUS ---
st.markdown("<p style='text-align:center; color:#22c55e;'>● Online • Ready to assist</p>", unsafe_allow_html=True)

st.markdown("### 💡 Try asking:")
col1, col2, col3 = st.columns(3)

if col1.button("Pricing"):
    question = "What are your pricing plans?"
    st.session_state.messages.append({"role": "user", "content": question})
    response = get_response(question)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
    
if col2.button("Services"):
    question = "What services do you offer?"
    st.session_state.messages.append({"role": "user", "content": question})
    response = get_response(question)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

if col3.button("Support"):
    question = "How can I contact support?"
    st.session_state.messages.append({"role": "user", "content": question})
    response = get_response(question)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()


# --- SESSION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! Ask me anything about our services."}
    ]

# --- CHAT UI ---
st.markdown("<div class='chat-card'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div style='display:flex; justify-content:flex-end'>
            <div class='user-msg'>{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style='display:flex; justify-content:flex-start'>
            <div class='bot-msg'>🤖 {msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- INPUT ---
user_input = st.chat_input("Ask about pricing, services, or support...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# --- FOOTER ---
st.markdown("""
<p style='text-align:center; color:gray; font-size:12px;'>
Powered by AI • Built with Machine Learning
</p>
""", unsafe_allow_html=True)