import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('../data/faq.csv')

vectorizer = pickle.load(open('../model/vectorizer.pkl', 'rb'))
X = pickle.load(open('../model/question_vectors.pkl', 'rb'))

st.set_page_config(page_title="FAQ Chatbot", page_icon=":robot_face:")

st.title("Business Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg['content'])


user_input = st.chat_input("Ask something...")

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    best_match_idx = similarities.argmax()
    return df.iloc[best_match_idx]['answer']

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)