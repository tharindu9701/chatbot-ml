import streamlit as st
import pandas as pd
from chatbot import get_response,train_model

st.set_page_config(page_title="AI Chatbot", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! Ask me anything about our services."}
    ]

st.markdown("""
<div style='
    background: linear-gradient(135deg, #1e293b, #2563eb);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
'>
    <h1 style='margin-bottom:10px;'>🤖 AI Customer Support</h1>
    <p style='opacity:0.9;'>Automate customer support instantly</p>
    <p style='color:#22c55e;'>● Online • Ready</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='color:#0f172a;'>📂 Upload Your Business FAQ</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "question" not in df.columns or "answer" not in df.columns:
        st.error("CSV must contain 'question' and 'answer' columns")
    else:
        vectorizer, X = train_model(df)

        st.session_state.df = df
        st.session_state.vectorizer = vectorizer
        st.session_state.X = X

        st.success("✅ Chatbot trained on your data!")


df = st.session_state.get("df")
vectorizer = st.session_state.get("vectorizer")
X = st.session_state.get("X")

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e293b 0%, #2563eb 100%);
}

.block-container {
    background: #f8fafc;
    border-radius: 20px;
    padding: 2rem;
    margin-top: 20px;
}

[data-testid="stFileUploader"] {
    color: #0f172a;
}

[data-testid="stFileUploader"] label {
    color: #0f172a ;
}

[data-testid="stFileUploader"] div {
    color: #0f172a;
}

[data-testid="stFileUploader"] button {
    color: white ;
    background-color: #2563eb;
    border-radius: 8px;
}


[data-testid="stFileUploader"] button:hover {
    background-color: #1d4ed8;
}


.block-container {
    max-width: 800px;
    margin: auto;
    padding-top: 2rem;
}


.chat-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.15);
    color: white;
}


.user-msg {
    background: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 14px;
    margin: 8px 0;
    max-width: 60%;
}


.bot-msg {
    background: #f1f5f9;
    color: #0f172a;
    padding: 12px 16px;
    border-radius: 14px;
    margin: 8px 0;
    max-width: 60%;
}


.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}


textarea, input {
    border-radius: 10px !important;
    border: 1px solid #e2e8f0 !important;
}


.quick-box {
    background: white;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 10px;
    font-weight: 500;
}


.title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #0f172a;
}


.subtitle {
    text-align: center;
    color: #64748b;
}


.status {
    text-align: center;
    color: #22c55e;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)




st.markdown("<p style='text-align:center; color:#22c55e;'>● Online • Ready to assist</p>", unsafe_allow_html=True)

st.markdown("""
<div style='
    background:#e2e8f0;
    padding:15px;
    border-radius:12px;
    text-align:center;
    margin-bottom: 10px;
    font-weight:500;
    color:#0f172a;
'>
💡 Quick Questions
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3, gap = "large")

if col1.button("Pricing"):
    question = "What are your pricing plans?"
    st.session_state.messages.append({"role": "user", "content": question})
    if df is not None:
        response = get_response(question, df, vectorizer, X)
    else:
        response = "Please upload a CSV file first."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
    
if col2.button("Services"):
    question = "What services do you offer?"
    st.session_state.messages.append({"role": "user", "content": question})
    if df is not None:
        response = get_response(question, df, vectorizer, X)
    else:
        response = "Please upload a CSV file first."
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

if col3.button("Support"):
    question = "How can I contact support?"
    st.session_state.messages.append({"role": "user", "content": question})
    if df is not None:
        response = get_response(question, df, vectorizer, X)
    else:
        response = "Please upload a CSV file first."
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()




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


user_input = st.chat_input("Ask about pricing, services, or support...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        if df is not None:
            response = get_response(user_input, df, vectorizer, X)
        else:
            response = "Please upload a CSV file first."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()


st.markdown("""
<p style='text-align:center; color:gray; font-size:12px;'>
Powered by AI • Built with Machine Learning
</p>
""", unsafe_allow_html=True)