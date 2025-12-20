import streamlit as st
import pickle
import string

import nltk
nltk.download('stopwords', quiet=True)  
from nltk.corpus import stopwords
STOP_WORDS = set(stopwords.words('english'))






with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return " ".join(words)

st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("Fake News Detection App")
st.write("Enter a news article below to check whether it is **Fake** or **Real**.")

news_input = st.text_area("Enter News Text", height=200)

if st.button("Check News"):
    if news_input.strip() == "":
        st.warning(" Please enter some text.")
    else:
        cleaned_news = clean_text(news_input)
        news_vector = vectorizer.transform([cleaned_news])
        prob = model.predict_proba(news_vector)[0]

      


        # if prob[0] == 1:
        #     st.success(" This news is REAL")
        # else:
        #     st.error(" This news is FAKE")
        st.write(f"Real News Probability: {prob[1]*100:.2f}%")
        st.write(f"Fake News Probability: {prob[0]*100:.2f}%")
