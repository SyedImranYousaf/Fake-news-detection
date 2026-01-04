import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split
from theme import init_theme, theme_toggle, apply_theme

init_theme()
theme_toggle()
apply_theme()
st.markdown("## 🧠 Model Insights")

with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")
fake["label"] = 0
true["label"] = 1
data = pd.concat([fake, true]).sample(frac=1)

X = vectorizer.transform(data["text"])
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

st.markdown("### 🎯 Figure 4: Confusion Matrix")
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(plt)
plt.clf()

st.markdown("### 📈 Figure 5: ROC Curve")
y_prob = model.predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
st.pyplot(plt)
plt.clf()

st.markdown("### 🔑 Figure 6: Feature Importance (Top Words)")

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

top_real = np.argsort(coefficients)[-15:]
top_fake = np.argsort(coefficients)[:15]

plt.figure()
plt.barh([feature_names[i] for i in top_real], coefficients[top_real])
plt.title("Words Indicating Real News")
st.pyplot(plt)
plt.clf()

plt.figure()
plt.barh([feature_names[i] for i in top_fake], coefficients[top_fake])
plt.title("Words Indicating Fake News")
st.pyplot(plt)
plt.clf()
