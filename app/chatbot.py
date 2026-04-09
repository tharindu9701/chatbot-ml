import pandas as pd
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

DATA_PATH = os.path.join(ROOT_DIR, "data", "faq.csv")
MODEL_PATH = os.path.join(ROOT_DIR, "model")


VECTORIZER_PATH = os.path.join(MODEL_PATH, "vectorizer.pkl")
VECTORS_PATH = os.path.join(MODEL_PATH, "question_vectors.pkl")


# Load model
vectorizer = pickle.load(open(VECTORIZER_PATH, 'rb'))
X = pickle.load(open(VECTORS_PATH, 'rb'))

@st.cache_resource
def load_data():
    df = pd.read_csv(DATA_PATH)
    vectorizer = pickle.load(open(VECTORIZER_PATH, 'rb'))
    X = pickle.load(open(VECTORS_PATH, 'rb'))
    return df, vectorizer, X


df, vectorizer, X = load_data()

def get_response(user_input):
    if not isinstance(user_input, str) or user_input.strip() == "":
        return "Please enter a valid question."

    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    best_match_idx = similarities.argmax()
    score = similarities[0][best_match_idx]

    if score < 0.3:
        return "Sorry, I don't understand your question."

    return df.iloc[best_match_idx]['answer']