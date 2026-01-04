import streamlit as st
import pickle, string, nltk
from nltk.corpus import stopwords
from theme import init_theme, theme_toggle, apply_theme

init_theme()
theme_toggle()
apply_theme()
nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return " ".join([w for w in text.split() if w not in STOP_WORDS])

with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.markdown("## 🔍 Fake News Checker")
news = st.text_area("Paste news article here", height=200)

if st.button("Analyze"):
    cleaned = clean_text(news)
    vec = vectorizer.transform([cleaned])
    prob = model.predict_proba(vec)[0]

    col1, col2 = st.columns(2)
    col1.metric("🟢 Real Probability", f"{prob[1]*100:.2f}%")
    col2.metric("🔴 Fake Probability", f"{prob[0]*100:.2f}%")
