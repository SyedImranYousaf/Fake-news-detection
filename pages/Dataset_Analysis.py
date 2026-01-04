import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import string, nltk
from nltk.corpus import stopwords
from collections import Counter
from theme import init_theme, theme_toggle, apply_theme

init_theme()
theme_toggle()
apply_theme()
nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return " ".join(w for w in text.split() if w not in STOP_WORDS)

st.markdown("## 📊 Dataset Analysis")

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")
fake["label"] = 0
true["label"] = 1
data = pd.concat([fake, true]).sample(frac=1).reset_index(drop=True)
data["clean_text"] = data["text"].apply(clean_text)

st.markdown("### 📌 Figure 1: Dataset Label Distribution")
plt.figure()
data["label"].value_counts().plot(kind="bar")
plt.xlabel("Label (0 = Fake, 1 = Real)")
plt.ylabel("Number of Articles")
st.pyplot(plt)
plt.clf()

st.markdown("### 🧾 Figure 2: News Length Comparison")
data["length"] = data["clean_text"].apply(lambda x: len(x.split()))

plt.figure()
plt.hist(data[data["label"]==0]["length"], bins=50, alpha=0.7, label="Fake")
plt.hist(data[data["label"]==1]["length"], bins=50, alpha=0.7, label="Real")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.legend()
st.pyplot(plt)
plt.clf()

st.markdown("### 🔤 Figure 3: Most Frequent Words")

words = " ".join(data["clean_text"]).split()
common_words = Counter(words).most_common(15)

labels, values = zip(*common_words)

plt.figure()
plt.barh(labels, values)
plt.xlabel("Frequency")
plt.ylabel("Words")
st.pyplot(plt)
plt.clf()
