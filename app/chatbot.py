import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def train_model(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["question"])
    return vectorizer, X


def get_response(user_input, df, vectorizer, X):
    if not isinstance(user_input, str) or user_input.strip() == "":
        return "Please enter a valid question."

    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)

    best_match_idx = similarities.argmax()
    score = similarities[0][best_match_idx]

    if score < 0.3:
        return "Sorry, I don't understand your question."

    return df.iloc[best_match_idx]["answer"]